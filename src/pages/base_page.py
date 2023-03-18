from playwright.sync_api import Page
from src.config import IMPLICIT_WAIT

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def click(self, selector: str):
        self.page.click(selector)

    def type(self, selector: str, text: str, clear_first: bool = False):
        if clear_first:
            self.page.fill(selector, '')
        self.page.type(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def is_element_visible(self, selector: str) -> bool:
        try:
            element = self.page.wait_for_selector(selector, timeout=IMPLICIT_WAIT, state="visible")
            return bool(element)
        except Exception:
            return False

    def is_element_not_visible(self, selector: str) -> bool:
        try:
            self.page.wait_for_selector(selector, timeout=IMPLICIT_WAIT, state="hidden")
            return True
        except Exception:
            return False

    def take_screenshot(self, file_name: str):
        self.page.screenshot(path=file_name)
