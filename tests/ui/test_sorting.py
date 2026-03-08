def test_sort_price_high_to_low(logged_in_page):
    page = logged_in_page

    # Pilih sort high to low
    page.locator(".product_sort_container").select_option("hilo")

    # Ambil semua harga
    prices = page.locator(".inventory_item_price").all_inner_texts()
    price_values = [float(p.replace("$", "")) for p in prices]

    # Validasi urutan benar
    assert price_values == sorted(price_values, reverse=True)