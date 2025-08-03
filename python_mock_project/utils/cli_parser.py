import argparse

def create_parser():
    """
    Tạo argument parser với các options đơn giản
    """
    parser = argparse.ArgumentParser(
        description="Chương trình test form submission",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python main/main_program.py --mode direct --headless
  python main/main_program.py --mode pytest --verbose
  python main/main_program.py --mode direct --count 5
  python main/main_program.py --mode direct --count 3 --delay 5
  python main/main_program.py --mode direct --browser firefox --count 3 --delay 2 --verbose
  python main/main_program.py --help
        """
    )
    
    # Option chọn cách chạy test
    parser.add_argument(
        '--mode',
        choices=['direct', 'pytest', 'menu'],
        default='menu',
        help='Cách chạy test: direct (trực tiếp), pytest (với pytest), menu (hiển thị menu lựa chọn)'
    )
    
    # Option chạy ẩn browser
    parser.add_argument(
        '--headless',
        action='store_true',
        help='Chạy browser ẩn (không hiển thị giao diện)'
    )
    
    # Option hiển thị chi tiết
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Hiển thị thông tin chi tiết khi chạy'
    )
    
    # Option chọn browser
    parser.add_argument(
        '--browser',
        choices=['chromium', 'firefox', 'webkit'],
        default='chromium',
        help='Loại browser sử dụng (mặc định: chromium)'
    )
    
    # Option chạy nhiều lần
    parser.add_argument(
        '--count',
        type=int,
        default=1,
        help='Số lần chạy test (mặc định: 1)'
    )
    
    # Option tạm dừng giữa các lần chạy
    parser.add_argument(
        '--delay',
        type=int,
        default=0,
        help='Số giây tạm dừng giữa các lần chạy test (mặc định: 0)'
    )
    
    return parser

def parse_arguments():
    """
    Parse arguments và trả về kết quả
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Hiển thị thông tin nếu verbose
    if args.verbose:
        print("=== Thông tin cấu hình ===")
        print(f"Mode: {args.mode}")
        print(f"Headless: {args.headless}")
        print(f"Browser: {args.browser}")
        print(f"Verbose: {args.verbose}")
        print(f"Count: {args.count}")
        print(f"Delay: {args.delay} giây")
        print("========================")
    
    return args

def get_user_choice_from_menu():
    """
    Hiển thị menu và nhận lựa chọn từ user (giống như code cũ)
    """
    print("Chọn cách chạy test:")
    print("1. Chạy trực tiếp (không cần pytest)")
    print("2. Chạy với pytest")
    
    while True:
        choice = input("Nhập lựa chọn (1 hoặc 2): ").strip()
        if choice == "1":
            return "direct"
        elif choice == "2":
            return "pytest"
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập 1 hoặc 2.")

def get_final_mode(args):
    """
    Xác định mode cuối cùng dựa trên arguments
    """
    if args.mode == "menu":
        # Nếu chọn menu, hiển thị menu cho user chọn
        return get_user_choice_from_menu()
    else:
        # Nếu đã chọn mode cụ thể, dùng luôn
        return args.mode
    
if __name__ == "__main__":
    # Test các function parser
    args = parse_arguments()
    print("Parsed arguments:", vars(args))