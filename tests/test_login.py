import pytest

from src.config import TEST_PASSWORD, TEST_USERNAME, BASE_URL
from src.pages.inventory_page import InventoryPage

@pytest.mark.parametrize("username", TEST_USERNAME)
def test_valid_login(login_page, username):
    login_page.go_to_url(BASE_URL)
    login_page.login(TEST_USERNAME, TEST_PASSWORD)

    # Verify that the user is logged in and redirected to the correct page
    inventory_page = InventoryPage(login_page.page)
    assert inventory_page.is_page_loaded(), f"User '{username}' should be logged in."

def test_invalid_login(login_page):
    login_page.go_to_url(BASE_URL)
    login_page.login("invalid_user", "wrong_password")

    # Verify that an error message is displayed
    assert login_page.is_error_message_visible(), "Error message should be visible for invalid login."
    assert login_page.is_page_loaded(), "Login page should be be still visible."

def test_empty_credentials(login_page):
    login_page.go_to_url(BASE_URL)
    login_page.login("", "")

    # Verify that an error message is displayed
    assert login_page.is_error_message_visible(), "Error message should be visible for empty credentials."
    assert login_page.is_page_loaded(), "Login page should be be still visible."
