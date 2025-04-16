import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from locators.cart_page_repo import CART_ROW_BY_NAME
from locators.product_page_repo import PROCESSOR_SLOW, RAM_2GB, HDD_320GB, PROCESSOR_EXPENSIVE, RAM_4GB_EXPENSIVE, HDD_400GB_EXPENSIVE


@pytest.mark.parametrize(
    "custom_computer_name, processor, ram, hdd",
    [
        ("Build your own cheap computer", PROCESSOR_SLOW, RAM_2GB, HDD_320GB),
        ("Build your own expensive computer", PROCESSOR_EXPENSIVE, RAM_4GB_EXPENSIVE, HDD_400GB_EXPENSIVE),
    ]
)
def test_full_shopping_cart_flow(page, custom_computer_name, processor, ram, hdd):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    # 1️⃣ Add Gift Card
    home.go_to_homepage()
    home.select_product("25 Virtual Gift Card")
    product.add_gift_card(
        recipient_name="Emma",
        recipient_email="emma@mail.com",
        sender_name="Albina",
        sender_email="albina.hakobyan7@gmail.com",
        quantity=1
    )

    # 2️⃣ Add Laptop from homepage
    home.go_to_homepage()
    home.add_laptop_from_homepage()

    # 3️⃣ Add Custom Computer (cheap or expensive based on param)
    home.go_to_homepage()
    home.select_product(custom_computer_name)
    product.add_custom_computer_to_cart(processor, ram, hdd)

    # ✅ Verify items in cart
    cart.go_to_cart()
    cart.verify_item_is_in_cart("$25 Virtual Gift Card")
    cart.verify_item_is_in_cart("14.1-inch Laptop")
    cart.verify_item_is_in_cart(custom_computer_name)

    # ❌ Remove one item
    cart.remove_item("14.1-inch Laptop")
    page.wait_for_timeout(1000)
    assert not cart.is_visible(CART_ROW_BY_NAME("14.1-inch Laptop"))

    # 🧹 Clear the cart
    cart.clear_cart()
    assert cart.is_cart_empty()
