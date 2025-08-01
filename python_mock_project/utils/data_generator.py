import random
from faker import Faker
from datetime import datetime 
import os
import json # Import json để in kết quả đẹp mắt

# Khởi tạo Faker để tạo dữ liệu giả
fake = Faker('en_US')

# Thiết lập seed để có thể tái tạo dữ liệu ngẫu nhiên cho mục đích gỡ lỗi
Faker.seed(42)

def generate_user_profile():
    """
    Tạo một hồ sơ người dùng ngẫu nhiên hoàn chỉnh để điền vào biểu mẫu.
    """
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    # Danh sách các lựa chọn có sẵn trong biểu mẫu
    genders = ['Male', 'Female', 'Other']
    
    # Điền các danh sách còn thiếu dựa trên các lựa chọn phổ biến trong form demo
    hobbies = ['Sports', 'Reading', 'Music'] 
    subjects = [
        'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Economics',
        'Biology', 'Arts', 'History'
    ]
    
    states = {
        "NCR": ["Delhi", "Gurgaon", "Noida"], # Điền các thành phố cho NCR
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    
    state_choice = random.choice(list(states.keys()))
    city_choice = random.choice(states[state_choice])

    # Tạo một file ảnh giả để tải lên
    # Đảm bảo file nằm trong cùng thư mục với script hoặc đường dẫn cụ thể
    picture_filename = "dummy_image.png"
    # Kiểm tra xem file đã tồn tại chưa để tránh tạo lại mỗi khi chạy
    if not os.path.exists(picture_filename):
        with open(picture_filename, "w") as f: # Tạo một file văn bản rỗng làm file dummy
            f.write("This is a dummy image file for testing purposes.")
        print(f"Created dummy image file: {picture_filename}") # Thông báo khi tạo file
    else:
        print(f"Dummy image file already exists: {picture_filename}")

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
        "gender": random.choice(genders),
        "mobile": fake.msisdn()[:10], # Lấy 10 chữ số đầu, phù hợp với số điện thoại Ấn Độ
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=60), # Tạo ngày sinh ngẫu nhiên
        "subjects": random.sample(subjects, k=random.randint(1, 3)), # Chọn 1-3 môn học ngẫu nhiên
        "hobbies": random.sample(hobbies, k=random.randint(1, 2)), # Chọn 1-2 sở thích ngẫu nhiên
        "picture_path": os.path.abspath(picture_filename), # Lấy đường dẫn tuyệt đối của file ảnh
        "address": fake.address().replace('\n', ', '), # Chuyển địa chỉ thành một dòng
        "state": state_choice,
        "city": city_choice
    }

if __name__ == '__main__':
    # Ví dụ cách sử dụng
    print("Generating user profile data...")
    user_data = generate_user_profile()
    
    # In dữ liệu ra console dưới dạng JSON để dễ đọc
    # default=str giúp chuyển đổi đối tượng datetime.date thành chuỗi trước khi serialize
    print(json.dumps(user_data, indent=4, default=str, ensure_ascii=False))

    print("\nData generation complete.")

