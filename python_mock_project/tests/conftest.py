import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """
    Pytest fixture để tạo browser page cho test
    """
    print("Setting up browser...")
    
    # Khởi tạo playwright
    playwright = sync_playwright().start()
    
    # Tạo browser (có thể thay đổi browser type)
    browser = playwright.chromium.launch(headless=False)
    
    # Tạo context và page
    context = browser.new_context()
    page = context.new_page()
    
    # Trả về page object cho test
    yield page
    
    # Cleanup sau khi test xong
    print("Cleaning up browser...")
    context.close()
    browser.close()
    playwright.stop()