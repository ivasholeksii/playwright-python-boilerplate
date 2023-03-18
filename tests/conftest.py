import pytest
from playwright.sync_api import sync_playwright
from src.config import BROWSER_TYPE, HEADLESS, SLOW_MO
from src.pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser_context():
    # Launch browser
    with sync_playwright() as playwright:
        browser = getattr(playwright, BROWSER_TYPE).launch(headless=HEADLESS, slow_mo=SLOW_MO)

        # Create a new context for each test session
        context = browser.new_context()

        yield context

        # Close browser after the test session is complete
        browser.close()

@pytest.fixture
def page(browser_context):
    # Create a new page for each test
    page = browser_context.new_page()

    yield page

    # Close page after the test is complete
    page.close()

@pytest.fixture
def login_page(page):
    # Instantiate the LoginPage for each test
    login_page = LoginPage(page)

    yield login_page
