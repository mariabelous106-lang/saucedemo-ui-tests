import pytest
from playwright.sync_api import Page


@pytest.fixture
def logged_in(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    return page


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()


def test_add_to_cart(logged_in: Page):
    page = logged_in
    page.click("text=Add to cart")
    page.click(".shopping_cart_link")
    assert page.locator(".cart_item").count() == 1


def test_complete_checkout(logged_in: Page):
    page = logged_in
    page.click("text=Add to cart")
    page.click(".shopping_cart_link")
    page.click("text=Checkout")
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "12345")
    page.click("text=Continue")
    page.click("text=Finish")
    assert page.locator("text=Thank you for your order").is_visible()


def test_sort_low_to_high(logged_in: Page):
    page = logged_in
    page.select_option("[data-test='product-sort-container']", "lohi")
    prices = page.locator(".inventory_item_price").all_text_contents()
    numeric = [float(p.replace("$", "")) for p in prices]
    assert numeric == sorted(numeric)
