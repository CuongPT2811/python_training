# Form Submission Test Automation

Công cụ tự động hóa test form submission sử dụng Playwright và Python. Dự án này giúp test form trên website DemoQA một cách tự động với nhiều tùy chọn linh hoạt.

## Tính năng chính

- **Nhiều chế độ chạy test**: Direct mode, Pytest mode, Menu tương tác
- **Cross-browser testing**: Hỗ trợ Chromium, Firefox, WebKit
- **Headless/Headed mode**: Có thể chạy ẩn hoặc hiển thị browser
- **Multiple test runs**: Chạy test nhiều lần với delay tùy chỉnh
- **Random data generation**: Tự động tạo dữ liệu giả để test
- **Logging & Reporting**: Ghi log chi tiết và lưu screenshot
- **CLI interface**: Giao diện dòng lệnh thân thiện

## Công nghệ sử dụng

Chi tiết các package và version xem trong `requirements.txt`:

- **Python 3.8+**: Ngôn ngữ lập trình chính
- **Playwright**: Framework tự động hóa browser
- **Pytest**: Framework testing
- **Faker**: Thư viện tạo dữ liệu giả

## Cài đặt

### Bước 1: Yêu cầu hệ thống
- Python 3.8 trở lên
- pip package manager
- Git (để clone project)

### Bước 2: Clone project
```bash
git clone <url-project-của-bạn>
cd form-submission-test
```

### Bước 3: Tạo virtual environment (khuyến nghị)
```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Bước 4: Cài đặt dependencies
```bash
# Cài đặt các package từ requirements.txt
pip install -r requirements.txt

# Cài đặt browsers cho Playwright
playwright install
```

### Bước 5: Kiểm tra cài đặt
```bash
# Kiểm tra Python và pip
python --version
pip --version

# Kiểm tra Playwright
playwright --version
```

## Hướng dẫn sử dụng

### Chạy lần đầu tiên (Menu tương tác)
```bash
python main/main_program.py
```
Chương trình sẽ hiển thị menu cho bạn chọn cách chạy test.

### Các cách chạy khác

#### 1. Chạy trực tiếp (Direct mode)
```bash
python main/main_program.py --mode direct
```

#### 2. Chạy với pytest
```bash
python main/main_program.py --mode pytest
```

#### 3. Chạy ẩn browser (nhanh hơn)
```bash
python main/main_program.py --mode direct --headless
```

#### 4. Chạy nhiều lần với delay
```bash
python main/main_program.py --mode direct --count 5 --delay 3
```

#### 5. Chạy với browser khác
```bash
python main/main_program.py --mode direct --browser firefox
```

#### 6. Hiển thị thông tin chi tiết
```bash
python main/main_program.py --mode direct --verbose
```

### Xem tất cả options
```bash
python main/main_program.py --help
```

## Kết quả test

Sau khi chạy test, bạn sẽ thấy:

1. **Console output**: Kết quả real-time trong terminal
2. **CSV log**: File `reports/test_submission_log.csv` chứa lịch sử test
3. **Screenshots**: Ảnh chụp màn hình kết quả trong `reports/`

## Cấu trúc project

```
project/
├── README.md  
│   ├── requirements.txt         # Dependencies
│   └──  README.md               # README.md
├── main/
│   └── main_program.py          # Main program
├── tests/
│   ├── conftest.py              # Pytest fixtures
│   └── test_form_submission.py  # Test logic chính
├── utils/
│   ├── cli_parser.py            # Xử lý CLI arguments
│   ├── data_generator.py        # Tạo dữ liệu giả
│   └── log_submission_result.py # Logging functionality
├── screenshots/
│   └── .png                     # Screenshots
└── reports/                    
    └── test_submission_log.csv  # Kết quả test
```

## Troubleshooting

### Lỗi thường gặp

1. **ModuleNotFoundError: No module named 'playwright'**
   ```bash
   pip install playwright
   playwright install
   ```

2. **Browser not found**
   ```bash
   playwright install chromium
   ```

3. **Permission denied**
   - Windows: Chạy cmd as Administrator
   - macOS/Linux: Dùng `sudo` nếu cần

4. **Test fail ngẫu nhiên**
   - Thử chạy với `--delay 2` để tăng thời gian chờ
   - Kiểm tra kết nối internet

### Debug

Để debug khi test fail:
```bash
# Chạy với verbose để xem chi tiết
python main/main_program.py --mode direct --verbose

# Chạy không headless để xem browser
python main/main_program.py --mode direct --headless false
```

## Phát triển thêm

### Thêm tính năng mới
1. Fork project
2. Tạo branch mới: `git checkout -b feature/ten-tinh-nang`
3. Code và test
4. Commit: `git commit -m "Add: mô tả tính năng"`
5. Push và tạo Pull Request

### Chạy test development
```bash
# Test riêng data generator
python utils/data_generator.py

# Test riêng CLI parser
python utils/cli_parser.py

# Chạy pytest trực tiếp
pytest tests/test_form_submission.py -v
```
## Tác giả
Tạo bởi CuongPT24 - Dự án thực hành Python automation testing

**Lưu ý**: Đây là project học tập, chỉ test trên trang demoqa.