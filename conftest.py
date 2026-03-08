import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture(scope="function")
def browser_page():
    """Fixture: launch browser, yield page, lalu close."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def logged_in_page(browser_page):
    """Fixture: buka SauceDemo dan login dulu sebelum test."""
    browser_page.goto(BASE_URL)
    browser_page.fill("#user-name", "standard_user")
    browser_page.fill("#password", "secret_sauce")
    browser_page.click("#login-button")
    browser_page.wait_for_url("**/inventory.html")
    return browser_page