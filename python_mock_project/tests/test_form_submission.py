
import pytest
from playwright.sync_api import Page, expect
from utils.data_generator import generate_user_profile
import time

# Target URL
URL = "https://demoqa.com/automation-practice-form"

first_name_ID =" #firstName"
last_name_ID = "#lastName"
user_email_ID = "#userEmail"
user_number_ID = "#userNumber"
date_of_birth_input_ID = "#dateOfBirthInput"
subjects_input_ID = "#subjectsInput"
upload_picture_ID = "#uploadPicture"
state_ID = "#state"
city_ID = "#city"
current_address_ID = "#currentAddress"
submit_ID = "#submit"


def test_successful_form_submission(page: Page):
    """
    Test form filling process, submit student registration form using CSS selectors
    """
    # 1. Generate random user data
    user_data = generate_user_profile()

    # 2. Go to web page
    page.goto(URL)
    # Remove ads to avoid elements being hidden
    page.evaluate("() => { document.querySelectorAll('#adplus-anchor,.adsbygoogle').forEach(el => el.remove()); }")

    # 3. Fill the text fields using CSS selectors with IDs
    page.locator(first_name_ID).fill(user_data["first_name"])
    page.locator(last_name_ID).fill(user_data["last_name"])
    page.locator(user_email_ID).fill(user_data["email"])
    page.locator(user_number_ID).fill(user_data["mobile"])
    page.locator(current_address_ID).fill(user_data["address"])

    # 4. Choose gender (Radio Button) using CSS selectors
    # Map gender to corresponding radio button labels
    gender_mapping = {
        "Male": "#gender-radio-1",
        "Female": "#gender-radio-2", 
        "Other": "#gender-radio-3"
    }
    
    # Click the label associated with the radio button (since radio inputs are hidden)
    gender_label_mapping = {
        "Male": "label[for='gender-radio-1']",
        "Female": "label[for='gender-radio-2']",
        "Other": "label[for='gender-radio-3']"
    }
    
    if user_data["gender"] in gender_label_mapping:
        page.locator(gender_label_mapping[user_data["gender"]]).click()

    # 5. Choose date of birth (Date Picker)
    dob_string = user_data["date_of_birth"].strftime('%d %b %Y')
    page.locator(date_of_birth_input_ID).fill(dob_string)
    page.keyboard.press("Enter")

    # 6. Choose the subjects
    subjects_input = page.locator(subjects_input_ID)
    for subject in user_data["subjects"]:
        subjects_input.fill(subject)
        subjects_input.press("Enter")

    # Scroll submit button into view to avoid element not visible/stable error
    page.locator(submit_ID).scroll_into_view_if_needed()

    # 7. Choose hobbies (Checkbox) using CSS selectors
    # Map hobbies to corresponding checkbox labels
    hobby_label_mapping = {
        "Sports": "label[for='hobbies-checkbox-1']",
        "Reading": "label[for='hobbies-checkbox-2']",
        "Music": "label[for='hobbies-checkbox-3']"
    }
    
    for hobby in user_data["hobbies"]:
        if hobby in hobby_label_mapping:
            # Use force=True to make sure clickable even if being hidden
            page.locator(hobby_label_mapping[hobby]).click(force=True)

    # 8. Upload picture
    page.locator(upload_picture_ID).set_input_files(user_data["picture_path"])

    # 9. Choose state -> city (Dependent Dropdowns)
    # Click state dropdown - use more reliable selector
    page.locator(state_ID).click()
    # Wait for dropdown to open
    page.wait_for_timeout(1000)
    # Select state option using text content
    page.get_by_text(user_data["state"], exact=True).click()
    
    # Wait for city options to load after state selection
    page.wait_for_timeout(1000)
    
    # Click city dropdown
    page.locator(city_ID).click()
    # Wait for city dropdown to open
    page.wait_for_timeout(1000)
    # Select city option using text content
    page.get_by_text(user_data["city"], exact=True).click()

    # 10. Submit the form
    page.locator(submit_ID).click()

    # 11. Validate result in the modal
    modal_title = page.locator("#example-modal-sizes-title-lg")
    expect(modal_title).to_be_visible(timeout=5000)
    expect(modal_title).to_have_text("Thanks for submitting the form")
    
    # Check important values in the result table
    student_name_row = page.locator("tbody tr:has-text('Student Name')")
    expect(student_name_row).to_contain_text(f"{user_data['first_name']} {user_data['last_name']}")
    
    # Check previously problematic fields
    subjects_row = page.locator("tbody tr:has-text('Subjects')")
    expect(subjects_row).to_contain_text(", ".join(user_data["subjects"]))

    hobbies_row = page.locator("tbody tr:has-text('Hobbies')")
    expect(hobbies_row).to_contain_text(", ".join(user_data["hobbies"]))

    state_city_row = page.locator("tbody tr:has-text('State and City')")
    expect(state_city_row).to_contain_text(f"{user_data['state']} {user_data['city']}")

    # 12. Take screenshot of the result
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f"reports/submission_result_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # 13. Close the modal
    page.locator("#closeLargeModal").click()