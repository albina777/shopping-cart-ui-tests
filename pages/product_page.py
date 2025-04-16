from pages.base_page import BasePage
from playwright.sync_api import expect
from locators.product_page_repo import (
    ADD_TO_CART_BUTTON,
    ADD_TO_CART_BUTTON_LAPTOP,
    RECIPIENT_NAME_INPUT,
    RECIPIENT_EMAIL_INPUT,
    SENDER_NAME_INPUT,
    SENDER_EMAIL_INPUT,
    QUANTITY_INPUT,
    PROCESSOR_SLOW,
    RAM_2GB,
    HDD_320GB,
    SUCCESS_NOTIFICATION
)

class ProductPage(BasePage):

    def add_gift_card(self, recipient_name, recipient_email, sender_name, sender_email, quantity=1):
        self.fill(RECIPIENT_NAME_INPUT, recipient_name)
        self.fill(RECIPIENT_EMAIL_INPUT, recipient_email)
        self.fill(SENDER_NAME_INPUT, sender_name)
        self.fill(SENDER_EMAIL_INPUT, sender_email)
        self.fill(QUANTITY_INPUT, str(quantity))
        self.click(ADD_TO_CART_BUTTON)
        self.page.wait_for_selector(SUCCESS_NOTIFICATION)

    def add_regular_laptop_to_card(self):
        self.click(ADD_TO_CART_BUTTON_LAPTOP)
        self.page.wait_for_selector(SUCCESS_NOTIFICATION)

    def add_custom_computer_to_cart(self, processor, ram, hdd):
        expect(self.page.locator(processor)).to_be_visible(timeout=10000)
        self.click(processor)
        self.click(ram)
        self.click(hdd)
        self.click(ADD_TO_CART_BUTTON)
        self.page.wait_for_selector(SUCCESS_NOTIFICATION)

