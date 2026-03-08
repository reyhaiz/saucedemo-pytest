def test_add_to_cart_and_checkout(logged_in_page):
    page = logged_in_page

    # Tambah item ke cart
    page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    # Validasi cart badge = 1
    assert page.locator(".shopping_cart_badge").inner_text() == "1"

    # Masuk ke cart
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")

    # Checkout
    page.locator("[data-test='checkout']").click()
    page.wait_for_url("**/checkout-step-one.html")

    # Isi form
    page.fill("[data-test='firstName']", "John")
    page.fill("[data-test='lastName']", "Doe")
    page.fill("[data-test='postalCode']", "12345")

    page.locator("[data-test='continue']").click()
    page.wait_for_url("**/checkout-step-two.html")

    page.locator("[data-test='finish']").click()
    page.wait_for_url("**/checkout-complete.html")

    # Validasi gambar Pony Express muncul
    assert page.locator(".pony_express").is_visible()