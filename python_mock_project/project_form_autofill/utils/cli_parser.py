import argparse

def create_parser():
    """
    Create argument parsers with simple options
    """
    parser = argparse.ArgumentParser(
        description="Test form submission program",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  python main/main_program.py --mode direct --headless
  python main/main_program.py --mode pytest --verbose
  python main/main_program.py --mode direct --count 5
  python main/main_program.py --mode direct --count 3 --delay 5
  python main/main_program.py --mode direct --browser firefox --count 3 --delay 2 --verbose
  python main/main_program.py --help
        """
    )
    
    #Option to choose test mode 
    parser.add_argument(
        '--mode',
        choices=['direct', 'pytest', 'menu'],
        default='menu',
        help='How to run: direct, pytest (with pytest), menu (display choose menu)'
    )
    
    #Option to run hidden browser
    parser.add_argument(
        '--headless',
        action='store_true',
        help='Run hidden browser (no interface display)'
    )
    
    #Option to display detail information
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Display detail information while running'
    )
    
    #Option to choose browser
    parser.add_argument(
        '--browser',
        choices=['chromium', 'firefox', 'webkit'],
        default='chromium',
        help='Browser used (default: chromium)'
    )
    
    #Option to run multiple time 
    parser.add_argument(
        '--count',
        type=int,
        default=1,
        help='Time to run test (default: 1)'
    )
    
    #Option to delay between tests
    parser.add_argument(
        '--delay',
        type=int,
        default=0,
        help='Seconds delay between test (default: 0)'
    )
    
    return parser

def parse_arguments():
    """
    Parse arguments and return result
    """
    parser = create_parser()
    args = parser.parse_args()
    
    #Display information if --verbose
    if args.verbose:
        print("=== Configuration ===")
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
    Display menu and get choice from user
    """
    print("Choose run mode for test:")
    print("1. Direct mode")
    print("2. Run with pytest")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            return "direct"
        elif choice == "2":
            return "pytest"
        else:
            print("Invalid choice! Please enter 1 or 2.")

def get_final_mode(args):
    """
    Determine final mode base on arguments
    """
    if args.mode == "menu":
        #If choosing menu, display the menu
        return get_user_choice_from_menu()
    else:
        #If a mode choosen, run
        return args.mode
    
if __name__ == "__main__":
    #Test parser function
    args = parse_arguments()
    print("Parsed arguments:", vars(args))