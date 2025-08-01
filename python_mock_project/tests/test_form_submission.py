import pytest
from playwright.sync_api import Page, expect
from utils.data_generator import generate_user_profile
import time

# URL của trang web mục tiêu
URL = "https://demoqa.com/automation-practice-form"

def test_successful_form_submission(page: Page):
    """
    Kiểm thử toàn bộ quy trình điền và gửi biểu mẫu đăng ký sinh viên.
    """
    # 1. Tạo dữ liệu người dùng ngẫu nhiên
    user_data = generate_user_profile()

    # 2. Mở trang web
    page.goto(URL)
    # Trang web có thể có quảng cáo che phủ, cần đóng chúng nếu có
    # Dòng này có thể cần thiết tùy thuộc vào trạng thái của trang web
    page.evaluate("() => { document.querySelectorAll('#adplus-anchor,.adsbygoogle').forEach(el => el.remove()); }")


    # 3. Điền các trường văn bản
    page.get_by_placeholder("First Name").fill(user_data["first_name"])
    page.get_by_placeholder("Last Name").fill(user_data["last_name"])
    page.get_by_placeholder("name@example.com").fill(user_data["email"])
    page.get_by_placeholder("Mobile Number").fill(user_data["mobile"])
    page.get_by_placeholder("Current Address").fill(user_data["address"])

    # 4. Chọn Giới tính (Radio Button)
    page.get_by_text(user_data["gender"], exact=True).check()

    # 5. Chọn Ngày sinh (Date Picker)
    # Chuyển đổi đối tượng datetime thành chuỗi theo định dạng "dd Mmm yyyy"
    dob_string = user_data["date_of_birth"].strftime('%d %b %Y')
    date_input = page.locator("#dateOfBirthInput")
    date_input.fill(dob_string)
    page.keyboard.press("Enter") # Đóng date picker

    # 6. Chọn Môn học (Autocomplete Input)
    subjects_input = page.locator("#subjectsInput")
    for subject in user_data["subjects"]:
        subjects_input.fill(subject)
        # Playwright sẽ tự động chờ phần tử đề xuất xuất hiện
        page.get_by_text(subject, exact=True).click()

    # 7. Chọn Sở thích (Checkbox)
    for hobby in user_data["hobbies"]:
        page.get_by_text(hobby, exact=True).check()

    # 8. Tải ảnh lên
    page.locator("#uploadPicture").set_input_files(user_data["picture_path"])

    # 9. Chọn Bang và Thành phố (Dependent Dropdowns)
    # Cần cuộn xuống để các phần tử này hiển thị trong viewport
    page.locator("#submit").scroll_into_view_if_needed()
    
    state_dropdown = page.locator("#state")
    state_dropdown.click()
    page.get_by_text(user_data["state"], exact=True).click()

    city_dropdown = page.locator("#city")
    city_dropdown.click()
    page.get_by_text(user_data["city"], exact=True).click()

    # 10. Gửi biểu mẫu
    page.locator("#submit").click()

    # 11. Xác thực kết quả trong Modal
    # Chờ cho modal xuất hiện
    modal_title = page.locator("#example-modal-sizes-title-lg")
    expect(modal_title).to_be_visible(timeout=5000)
    expect(modal_title).to_have_text("Thanks for submitting the form")
    
    # Kiểm tra một vài giá trị quan trọng
    student_name_row = page.locator("tbody tr", has_text="Student Name")
    expect(student_name_row).to_contain_text(f"{user_data['first_name']} {user_data['last_name']}")
    
    email_row = page.locator("tbody tr", has_text="Student Email")
    expect(email_row).to_contain_text(user_data["email"])

    # 12. Chụp ảnh màn hình kết quả
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f"reports/submission_result_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # 13. Đóng modal
    page.locator("#closeLargeModal").click()