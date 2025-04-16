from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str, timeout: int = 30000):  # allow custom timeout
        self.page.goto(url, timeout=timeout)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()
