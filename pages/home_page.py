from pages.base_page import BasePage
from playwright.sync_api import expect
from locators.home_page_repo import (
    ADD_LAPTOP_BUTTON,
    ADD_GIFT_CARD_BUTTON,
    ADD_BUILD_YOUR_OWN_CHEAP_COMPUTER
)

class HomePage(BasePage):
    HOMEPAGE_URL = "https://demowebshop.tricentis.com/"

    def go_to_homepage(self):
        self.page.goto(self.HOMEPAGE_URL, timeout=60000)
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(self.HOMEPAGE_URL)

    def select_product(self, product_name: str):
        self.click(f"text={product_name}")

    def add_laptop_from_homepage(self):
        self.click(ADD_LAPTOP_BUTTON)
        self.page.wait_for_selector("div.bar-notification.success")

    def add_gift_card_from_homepage(self):
        self.click(ADD_GIFT_CARD_BUTTON)
        self.page.wait_for_selector("div.bar-notification.success")

    def open_build_your_own_computer_page(self):
        self.click(ADD_BUILD_YOUR_OWN_CHEAP_COMPUTER)
