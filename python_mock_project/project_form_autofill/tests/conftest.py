import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """
    Pytest fixture to create browser for test
    """
    print("Setting up browser...")
    
    #Init playwright
    playwright = sync_playwright().start()
    
    #Create browser (can change browser type)
    browser = playwright.chromium.launch(headless=False)
    
    #Create context and page
    context = browser.new_context()
    page = context.new_page()
    
    #Return page object for test
    yield page
    
    #Cleanup after test
    print("Cleaning up browser...")
    context.close()
    browser.close()
    playwright.stop()