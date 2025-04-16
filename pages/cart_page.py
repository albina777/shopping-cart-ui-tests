from pages.base_page import BasePage
from locators.cart_page_repo import (
    CART_LINK,
    REMOVE_CHECKBOX,
    UPDATE_CART_BUTTON,
    CART_ROW_BY_NAME,
    CART_EMPTY_TEXT
)

class CartPage(BasePage):
    def go_to_cart(self):
        self.click(CART_LINK)

    def verify_item_is_in_cart(self, item_name):
        assert self.is_visible(CART_ROW_BY_NAME(item_name))

    def remove_item(self, item_name: str):
        row = self.page.locator(f"//a[text()='{item_name}']/../..")
        row.locator(REMOVE_CHECKBOX).click()
        self.click(UPDATE_CART_BUTTON)

#removing all elements
    def clear_cart(self):
        checkboxes = self.page.locator(REMOVE_CHECKBOX)
        count = checkboxes.count()
        for i in range(count):
            checkboxes.nth(i).click()
        self.click(UPDATE_CART_BUTTON)


    def is_cart_empty(self):
        return "Your Shopping Cart is empty!" in self.get_text(CART_EMPTY_TEXT)
    

    def wait_until_item_removed(self, item_name: str, timeout=5000):
        self.page.wait_for_selector(CART_ROW_BY_NAME(item_name), state="detached", timeout=timeout)

