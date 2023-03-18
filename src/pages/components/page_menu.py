from src.pages.base_page import BasePage
from src.config import BASE_URL

class PageMenu(BasePage):
    # Locators
    _logout_link = "#logout_sidebar_link-burger-menu-btn"

    # Navigate to the login page
    def logout(self):
        self._logout_link.click()

