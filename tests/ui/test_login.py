BASE_URL = "https://www.saucedemo.com"

def test_login_valid(browser_page):
    browser_page.goto(BASE_URL)
    browser_page.fill("#user-name", "standard_user")
    browser_page.fill("#password", "secret_sauce")
    browser_page.click("#login-button")
    assert "inventory.html" in browser_page.url

def test_login_wrong_password(browser_page):
    browser_page.goto(BASE_URL)
    browser_page.fill("#user-name", "standard_user")
    browser_page.fill("#password", "wrongpassword")
    browser_page.click("#login-button")
    assert browser_page.locator("[data-test='error']").is_visible()

def test_login_wrong_username(browser_page):
    browser_page.goto(BASE_URL)
    browser_page.fill("#user-name", "wrong_user")
    browser_page.fill("#password", "secret_sauce")
    browser_page.click("#login-button")
    assert browser_page.locator("[data-test='error']").is_visible()

def test_login_empty_fields(browser_page):
    browser_page.goto(BASE_URL)
    browser_page.click("#login-button")
    assert browser_page.locator("[data-test='error']").is_visible()

def test_login_long_input(browser_page):
    browser_page.goto(BASE_URL)
    long_text = "a" * 500
    browser_page.fill("#user-name", long_text)
    browser_page.fill("#password", long_text)
    browser_page.click("#login-button")
    assert browser_page.locator("[data-test='error']").is_visible()