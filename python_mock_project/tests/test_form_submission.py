import pytest
from playwright.sync_api import Page, expect
from utils.data_generator import generate_user_profile
from utils.log_submission_result import FormTestLogger
import time
import importlib
import sys
import random

#Force reload data_generator module to avoid caching
if 'utils.data_generator' in sys.modules:
    importlib.reload(sys.modules['utils.data_generator'])
    from utils.data_generator import generate_user_profile

#Target URL
URL = "https://demoqa.com/automation-practice-form"

#ID for locators
first_name_ID = "#firstName"
last_name_ID = "#lastName"
user_email_ID = "#userEmail"
user_number_ID = "#userNumber"
date_of_birth_ID = "#dateOfBirthInput"
subject_input_ID = "#subjectsInput"
uoload_picture_ID = "#uploadPicture"
state_ID = "#state"
city_ID = "#city"
current_address_ID = "#currentAddress"
submit_ID = "#submit"
close_large_modal_ID = "#closeLargeModal"


def generate_and_validate_user_data():
    """
    Generate random user profile data and validate it.
    
    Returns:
        tuple: (user_data dict, logger instance, validation_result tuple)
        
    Raises:
        pytest.fail: If generated data is missing required fields
    """
    logger = FormTestLogger()
    
    #Reset random seed to ensure different data each time
    random.seed()
    
    print(f"Current timestamp: {time.time()}")

    user_data = generate_user_profile()

    print("=== Generated User Data ===")
    print(f"First Name: {user_data.get('first_name', 'MISSING')}")
    print(f"Last Name: {user_data.get('last_name', 'MISSING')}")
    print(f"Email: {user_data.get('email', 'MISSING')}")
    print(f"Gender: {user_data.get('gender', 'MISSING')}")
    print(f"Mobile: {user_data.get('mobile', 'MISSING')}")
    print(f"Date of Birth: {user_data.get('date_of_birth', 'MISSING')}")
    print(f"Subjects: {user_data.get('subjects', 'MISSING')}")
    print(f"Hobbies: {user_data.get('hobbies', 'MISSING')}")
    print(f"State: {user_data.get('state', 'MISSING')}")
    print(f"City: {user_data.get('city', 'MISSING')}")
    print(f"Address: {user_data.get('address', 'MISSING')}")
    print(f"Picture Path: {user_data.get('picture_path', 'MISSING')}")
    print("==========================")
    
    #Start test logging
    logger.start_test(user_data)
    
    #Validate user data
    is_valid, missing_fields = logger.validate_form_data(user_data)
    print(f"=== Validation Result ===")
    print(f"Is Valid: {is_valid}")
    print(f"Missing Fields: {missing_fields}")
    print("========================")
    
    if not is_valid:
        logger.end_test(status="fail", missing_fields=missing_fields)
        pytest.fail(f"Generated user data is missing required fields: {', '.join(missing_fields)}")
    
    return user_data, logger, (is_valid, missing_fields)

def navigate_to_page(page: Page):
    """
    Navigate to the target URL and remove ads that might interfere with elements.
    
    Args:
        page (Page): Playwright page instance
    """
    page.goto(URL)
    #Remove ads to avoid elements being hidden
    page.evaluate("() => { document.querySelectorAll('#adplus-anchor,.adsbygoogle').forEach(el => el.remove()); }")

def fill_hard_info(page: Page, user_data: dict):
    select_subjects(page, user_data["subjects"])
    page.wait_for_timeout(2000)  #Small delay to ensure subject is added
    select_hobbies(page, user_data["hobbies"])
    page.wait_for_timeout(2000)  #Small delay to ensure subject is added
    upload_picture(page, user_data["picture_path"])
    select_state_and_city(page, user_data["state"], user_data["city"])

def fill_basic_info(page: Page, user_data: dict):
    """
    Fill the basic text input fields in the form.
    
    Args:
        page (Page): Playwright page instance
        user_data (dict): Dictionary containing user information
    """
    page.locator(first_name_ID).fill(user_data["first_name"])
    page.locator(last_name_ID).fill(user_data["last_name"])
    page.locator(user_email_ID).fill(user_data["email"])
    page.locator(user_number_ID).fill(user_data["mobile"])
    page.locator(current_address_ID).fill(user_data["address"])

def select_gender(page: Page, gender: str):
    """
    Select gender radio button based on the provided gender value.
    
    Args:
        page (Page): Playwright page instance
        gender (str): Gender value ("Male", "Female", or "Other")
    """
    #Map gender to corresponding radio button labels
    gender_label_mapping = {
        "Male": "label[for='gender-radio-1']",
        "Female": "label[for='gender-radio-2']",
        "Other": "label[for='gender-radio-3']"
    }
    
    if gender in gender_label_mapping:
        page.locator(gender_label_mapping[gender]).click()

def select_date_of_birth(page: Page, date_of_birth):
    """
    Select date of birth using the date picker.
    
    Args:
        page (Page): Playwright page instance
        date_of_birth: Date object representing the birth date
    """
    dob_string = date_of_birth.strftime('%d %b %Y')
    page.locator(date_of_birth_ID).fill(dob_string)
    page.keyboard.press("Enter")

def select_subjects(page: Page, subjects: list):
    """
    Select subjects from the autocomplete dropdown.
    
    Args:
        page (Page): Playwright page instance
        subjects (list): List of subject names to select
    """
    print(f"=== Filling Subjects: {subjects} ===")
    subjects_input = page.locator(subject_input_ID)
    for subject in subjects:
        print(f"Filling subject: {subject}")
        subjects_input.click()
        page.wait_for_timeout(500)  #Wait after click
        #Using fill() then Enter cause Autocomplete not working -> Missing a subject
        #Using type() with delay ensure dropdown available to choose by Enter
        subjects_input.type(subject, delay=50) 
        page.wait_for_timeout(1000)  #Wait for autocomplete dropdown
        subjects_input.press("Enter")
        page.wait_for_timeout(2000)  #Wait for subject to be added

def select_hobbies(page: Page, hobbies: list):
    """
    Select hobbies by clicking the corresponding checkboxes.
    
    Args:
        page (Page): Playwright page instance
        hobbies (list): List of hobby names to select
    """
    print(f"=== Filling Hobbies: {hobbies} ===")
    
    #Map hobbies to corresponding checkbox labels
    hobby_label_mapping = {
        "Sports": "label[for='hobbies-checkbox-1']",
        "Reading": "label[for='hobbies-checkbox-2']",
        "Music": "label[for='hobbies-checkbox-3']"
    }
    
    #Scroll submit button into view to avoid element not visible/stable error
    page.locator(submit_ID).scroll_into_view_if_needed()
    
    for hobby in hobbies:
        if hobby in hobby_label_mapping:
            print(f"Clicking hobby: {hobby}")
            #Use force=True to make sure clickable even if being hidden
            page.locator(hobby_label_mapping[hobby]).click(force=True)
            page.wait_for_timeout(2000)  #Small delay

def upload_picture(page: Page, picture_path: str):
    """
    Upload a picture file using the file input.
    
    Args:
        page (Page): Playwright page instance
        picture_path (str): Path to the picture file to upload
    """
    page.locator(uoload_picture_ID).set_input_files(picture_path)

def select_state_and_city(page: Page, state: str, city: str):
    """
    Select state and city from dependent dropdown menus.
    
    Args:
        page (Page): Playwright page instance
        state (str): State name to select
        city (str): City name to select
    """
    print(f"=== Filling State: {state}, City: {city} ===")
    
    #Click state dropdown
    page.locator(state_ID).click()
    page.wait_for_timeout(2000)  #Wait for dropdown to open
    
    #Select state option using text content
    print(f"Selecting state: {state}")
    page.get_by_text(state, exact=True).click()
    
    #Wait for city options to load after state selection
    page.wait_for_timeout(2000)
    
    #Click city dropdown
    page.locator(city_ID).click()
    page.wait_for_timeout(2000)  #Wait for city dropdown to open
    
    #Select city option using text content
    print(f"Selecting city: {city}")
    page.get_by_text(city, exact=True).click()

def validate_filled_data(page: Page):
    """
    Validate that the form fields have been properly filled before submission.
    
    Args:
        page (Page): Playwright page instance
    """
    print("=== Before submitting, checking filled values ===")
    
    #Check if important fields are actually filled
    filled_subjects = page.locator("#subjectsContainer .subjects-auto-complete__multi-value__label").count()
    filled_hobbies = page.locator("input[type='checkbox'][id^='hobbies-checkbox']:checked").count()
    filled_state = page.locator("#state .css-1uccc91-singleValue").text_content()
    filled_city = page.locator("#city .css-1uccc91-singleValue").text_content()
    
    print(f"Filled subjects count: {filled_subjects}")
    print(f"Filled hobbies count: {filled_hobbies}")
    print(f"Filled state: {filled_state}")
    print(f"Filled city: {filled_city}")
    print("=============================================")

def submit_form_and_validate_result(page: Page, user_data: dict):
    """
    Submit the form and validate the result in the modal dialog.
    
    Args:
        page (Page): Playwright page instance
        user_data (dict): Dictionary containing user information for validation
    """
    #Submit the form
    page.locator(submit_ID).click()
    
    #Validate result in the modal
    modal_title = page.locator("#example-modal-sizes-title-lg")
    expect(modal_title).to_be_visible(timeout=5000)
    expect(modal_title).to_have_text("Thanks for submitting the form")
    
    #Check important values in the result table
    student_name_row = page.locator("tbody tr:has-text('Student Name')")
    expect(student_name_row).to_contain_text(f"{user_data['first_name']} {user_data['last_name']}")
    
    #Check previously problematic fields
    subjects_row = page.locator("tbody tr:has-text('Subjects')")
    expect(subjects_row).to_contain_text(", ".join(user_data["subjects"]))

    hobbies_row = page.locator("tbody tr:has-text('Hobbies')")
    expect(hobbies_row).to_contain_text(", ".join(user_data["hobbies"]))

    state_city_row = page.locator("tbody tr:has-text('State and City')")
    expect(state_city_row).to_contain_text(f"{user_data['state']} {user_data['city']}")

def take_screenshot(page: Page):
    """
    Take a screenshot of the current page and save it with timestamp.
    
    Args:
        page (Page): Playwright page instance
        
    Returns:
        str: Path to the saved screenshot
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f"screenshots/submission_result_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    return screenshot_path

def close_modal(page: Page):
    """
    Close the result modal dialog.
    
    Args:
        page (Page): Playwright page instance
    """
    page.locator(close_large_modal_ID).click()

def handle_test_failure(logger: FormTestLogger, error: Exception):
    """
    Handle test failure by logging appropriate error information.
    
    Args:
        logger (FormTestLogger): Logger instance for recording test results
        error (Exception): The exception that caused the test failure
    """
    error_message = str(error)
    print(f"Test failed with error: {error_message}")
    
    #Store fields that might cause failure tests
    failed_fields = []
    
    #Check if it's a validation/submission/fields error
    if "validation" in error_message.lower():
        failed_fields = ["Form validation failed"]
    elif "modal" in error_message.lower() or "submit" in error_message.lower():
        failed_fields = ["Form submission failed"]
    elif "locator" in error_message.lower():
        failed_fields = ["Element not found"]
    else:
        failed_fields = ["Unknown error"]
    
    #Log the failure
    logger.end_test(status="fail", missing_fields=failed_fields)

def test_form_submission(page: Page):
    """
    Main test function that orchestrates the complete form submission test.
    
    Args:
        page (Page): Playwright page instance
    """
    try:
        #Generate and validate user data
        user_data, logger, _ = generate_and_validate_user_data()
        
        #Navigate to the page
        navigate_to_page(page)

        #Fill harder form sections
        fill_hard_info(page, user_data)
        
        #Fill basic form sections
        fill_basic_info(page, user_data)
        select_gender(page, user_data["gender"])
        select_date_of_birth(page, user_data["date_of_birth"])

        #Validate filled data before submission
        validate_filled_data(page)
        
        #Submit form and validate result
        submit_form_and_validate_result(page, user_data)
        
        #Take screenshot
        take_screenshot(page)
        
        #Close modal
        close_modal(page)
        
        #Log success
        logger.end_test(status="success")
        
    except Exception as e:
        #Handle any errors during test execution
        handle_test_failure(logger, e)
        #Re-raise the exception to fail the test
        raise


if __name__ == "__main__":
    """
    Main execution block for running the form submission test standalone.
    Note: This requires proper Playwright setup and page context.
    """
    print("This test requires Playwright page context.")
    print("Run using: pytest test_form_submission.py")
    print("Or integrate with your existing test framework.")