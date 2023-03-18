from src.pages.base_page import BasePage
from src.config import BASE_URL
from src.pages.components.page_menu import PageMenu

class InventoryPage(BasePage):
    
    _page_menu: PageMenu

    # Locators
    _hamburger_menu = "#react-burger-menu-btn"
    _basket_icon = "#shopping_cart_container"

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.hamburger_menu = page.locator(self._hamburger_menu)
        self.basket_icon = page.locator(self._basket_icon)

    # Navigate to the login page
    def navigate_to_login(self):
        self.go_to_url(BASE_URL + "/inventory.html")

    def is_page_loaded(self) -> bool:
        return self.is_element_visible(self._basket_icon)
    
    def logout(self):
        self._page_menu.click()
        self._page_menu.logout()
