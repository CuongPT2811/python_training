import sys
import os
import time
from playwright.sync_api import sync_playwright

#Add path to import module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#Import test function and CLI parser
from tests.test_form_submission import test_form_submission
from utils.cli_parser import parse_arguments, get_final_mode

def create_page_manually(browser_type="chromium", headless=False):
    """
    Create page object like pytest fixture
    """
    playwright = sync_playwright().start()
    
    #Choose browser
    if browser_type == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:  #default chromium
        browser = playwright.chromium.launch(headless=headless)
    
    context = browser.new_context()
    page = context.new_page()
    
    return playwright, browser, context, page

def run_test_directly(args):
    """
    Run test directly with page browser 
    """
    print("=== Run test directly ===")
    
    #Create page object with settings from arguments
    playwright, browser, context, page = create_page_manually(
        browser_type=args.browser,
        headless=args.headless
    )
    
    try:
        #Call test function with page object
        test_form_submission(page)
        print("=== Test completed successfully! ===")
        return True
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False
        
    finally:
        #Cleanup
        context.close()
        browser.close()
        playwright.stop()

def run_test_with_pytest(args):
    """
    Run test with pytest (need conftest.py file)
    """
    import pytest
    
    print("=== Run test with pytest ===")
    
    test_file = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test_form_submission.py')
    
    pytest_args = [test_file]
    
    #Add verbose if requested
    if args.verbose:
        pytest_args.extend(['-v', '-s'])
    
    pytest_args.append('--tb=short')
    
    exit_code = pytest.main(pytest_args)
    return exit_code == 0

def run_multiple_tests(args, final_mode):
    """
    Run multiple tests and summarize results 
    """
    total_runs = args.count
    successful_runs = 0
    failed_runs = 0
    delay_seconds = args.delay
    
    print(f"=== Start running {total_runs} test ===")
    if delay_seconds > 0:
        print(f"Delay {delay_seconds} second between test")
    
    for run_number in range(1, total_runs + 1):
        print(f"\n--- Run no {run_number}/{total_runs} ---")
        
        try:
            #Run test based on chosen mode
            if final_mode == "direct":
                success = run_test_directly(args)
            elif final_mode == "pytest":
                success = run_test_with_pytest(args)
            else:
                print("Invalid mode!")
                success = False
            
            #Đếm kết quả
            if success:
                successful_runs += 1
                print(f"Run no {run_number}: SUCCESS")
            else:
                failed_runs += 1
                print(f"Run no {run_number}: FAILED")
                
        except Exception as e:
            failed_runs += 1
            print(f"✗ Run no {run_number}: Error - {str(e)}")
        
        #Delay between test except last run
        if delay_seconds > 0 and run_number < total_runs:
            print(f"Delay {delay_seconds} second before next test...")
            time.sleep(delay_seconds)
    
    #Summarize
    print(f"\n=== SUMMARIZE ===")
    print(f"Total tests: {total_runs}")
    print(f"Success: {successful_runs}")
    print(f"Failed: {failed_runs}")
    print(f"Success rate: {(successful_runs/total_runs)*100:.1f}%")
    print("================")
    
    #Return true if all tests success
    return failed_runs == 0

def main():
    """
    Main program using CLI command
    """
    try:
        #Parse arguments from command line
        args = parse_arguments()
        
        #Determine final mode 
        final_mode = get_final_mode(args)
        
        #Check count > 1, run multiple tests
        if args.count > 1:
            success = run_multiple_tests(args, final_mode)
        else:
            #Run test 1 time like usua;
            if final_mode == "direct":
                success = run_test_directly(args)
            elif final_mode == "pytest":
                success = run_test_with_pytest(args)
            else:
                print("Invalid mode!")
                return False
            
        return success
        
    except Exception as e:
        print(f"Error while running test: {str(e)}")
        return False

if __name__ == "__main__":
    print("Run main program with CLI arguments...")
    success = main()
    if success:
        print("Program completed successfully!")
    else:
        print("Program has error!")
        sys.exit(1)