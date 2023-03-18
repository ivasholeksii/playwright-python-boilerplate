from src.pages.base_page import BasePage
from src.config import BASE_URL

class LoginPage(BasePage):
    # Locators
    _username_input = "#user-name"
    _password_input = "#password"
    _login_button = "#login-button"
    _error_message_container = ".error-message-container"

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator(self._username_input)
        self.password_input = page.locator(self._password_input)
        self.login_button = page.locator(self._login_button)

    # Navigate to the login page
    def navigate_to_login(self):
        self.go_to_url(BASE_URL)

    # Login method
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_page_loaded(self) -> bool:
        return self.is_element_visible(self._login_button)

    def get_error_message(self) -> str:
        return self.get_text(self._error_message_container)

    def is_error_message_visible(self) -> bool:
        return self.is_element_visible(self._error_message_container)
