import sys
import os
import time
from playwright.sync_api import sync_playwright

# Thêm đường dẫn để import các module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import test function và CLI parser
from tests.test_form_submission import test_form_submission
from utils.cli_parser import parse_arguments, get_final_mode

def create_page_manually(browser_type="chromium", headless=False):
    """
    Tạo page object giống như pytest fixture
    """
    playwright = sync_playwright().start()
    
    # Chọn loại browser
    if browser_type == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:  # mặc định chromium
        browser = playwright.chromium.launch(headless=headless)
    
    context = browser.new_context()
    page = context.new_page()
    
    return playwright, browser, context, page

def run_test_directly(args):
    """
    Chạy test function trực tiếp với page object tự tạo
    """
    print("=== Chạy test trực tiếp ===")
    
    # Tạo page object với settings từ arguments
    playwright, browser, context, page = create_page_manually(
        browser_type=args.browser,
        headless=args.headless
    )
    
    try:
        # Gọi test function với page object
        test_form_submission(page)
        print("=== Test hoàn thành thành công! ===")
        return True
        
    except Exception as e:
        print(f"Test thất bại: {str(e)}")
        return False
        
    finally:
        # Cleanup
        context.close()
        browser.close()
        playwright.stop()

def run_test_with_pytest(args):
    """
    Chạy test bằng pytest (cần conftest.py)
    """
    import pytest
    
    print("=== Chạy test bằng pytest ===")
    
    test_file = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test_form_submission.py')
    
    pytest_args = [test_file]
    
    # Thêm verbose nếu được yêu cầu
    if args.verbose:
        pytest_args.extend(['-v', '-s'])
    
    pytest_args.append('--tb=short')
    
    exit_code = pytest.main(pytest_args)
    return exit_code == 0

def run_multiple_tests(args, final_mode):
    """
    Chạy test nhiều lần và tổng kết kết quả
    """
    total_runs = args.count
    successful_runs = 0
    failed_runs = 0
    delay_seconds = args.delay
    
    print(f"=== Bắt đầu chạy {total_runs} lần test ===")
    if delay_seconds > 0:
        print(f"Sẽ tạm dừng {delay_seconds} giây giữa các lần chạy")
    
    for run_number in range(1, total_runs + 1):
        print(f"\n--- Lần chạy {run_number}/{total_runs} ---")
        
        try:
            # Chạy test theo mode đã chọn
            if final_mode == "direct":
                success = run_test_directly(args)
            elif final_mode == "pytest":
                success = run_test_with_pytest(args)
            else:
                print("Mode không hợp lệ!")
                success = False
            
            # Đếm kết quả
            if success:
                successful_runs += 1
                print(f"✓ Lần chạy {run_number}: THÀNH CÔNG")
            else:
                failed_runs += 1
                print(f"✗ Lần chạy {run_number}: THẤT BẠI")
                
        except Exception as e:
            failed_runs += 1
            print(f"✗ Lần chạy {run_number}: LỖI - {str(e)}")
        
        # Tạm dừng giữa các lần chạy (trừ lần cuối)
        if delay_seconds > 0 and run_number < total_runs:
            print(f"Tạm dừng {delay_seconds} giây trước lần chạy tiếp theo...")
            time.sleep(delay_seconds)
    
    # Tổng kết
    print(f"\n=== TỔNG KẾT ===")
    print(f"Tổng số lần chạy: {total_runs}")
    print(f"Thành công: {successful_runs}")
    print(f"Thất bại: {failed_runs}")
    print(f"Tỷ lệ thành công: {(successful_runs/total_runs)*100:.1f}%")
    print("================")
    
    # Trả về True nếu tất cả đều thành công
    return failed_runs == 0

def main():
    """
    Hàm main - sử dụng CLI arguments
    """
    try:
        # Parse arguments từ command line
        args = parse_arguments()
        
        # Xác định mode cuối cùng (có thể từ args hoặc từ menu)
        final_mode = get_final_mode(args)
        
        # Kiểm tra nếu count > 1, chạy multiple tests
        if args.count > 1:
            success = run_multiple_tests(args, final_mode)
        else:
            # Chạy test 1 lần như bình thường
            if final_mode == "direct":
                success = run_test_directly(args)
            elif final_mode == "pytest":
                success = run_test_with_pytest(args)
            else:
                print("Mode không hợp lệ!")
                return False
            
        return success
        
    except Exception as e:
        print(f"Lỗi khi chạy test: {str(e)}")
        return False

if __name__ == "__main__":
    print("Chạy main program với CLI arguments...")
    success = main()
    if success:
        print("Program đã chạy xong thành công!")
    else:
        print("Program gặp lỗi!")
        sys.exit(1)