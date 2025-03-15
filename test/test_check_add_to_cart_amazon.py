import time
import os
import uuid
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_to_cart():
    # WebDriver başlat
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Amazon aç
        driver.get("https://www.amazon.com.tr/")

        # Ana sayfada olduğunu doğrula
        assert "Amazon" in driver.title
        # Bilerek test bozdum Screen Shot için düşündüm.
        # assert "YANLIŞ METİN" in driver.title  # Burası hata verecek

        # Arama yap
        home_page.search_product("samsung")
        time.sleep(5)

        # Sonuçları doğrula
        assert "samsung" in driver.page_source.lower()

        # 2. sayfaya git
        search_results_page.go_to_second_page()
        time.sleep(5)

        # Şu an 2. sayfada olduğunu doğrulua
        assert "page=2" in driver.current_url

        # 3. ürüne git
        search_results_page.go_to_third_product()
        time.sleep(5)

        # Ürün sayfasında olduğunu doğrula
        assert "amazon.com.tr" in driver.current_url

        # Sepete ekle
        product_page.add_to_cart()
        time.sleep(5)

        # Sepete git
        product_page.go_to_cart()
        time.sleep(5)

        # Sepette ürün olduğunu doğrula
        assert cart_page.verify_item_in_cart(), "HATA: Ürün sepette görünmüyor!"

        # Ürünü sil ve doğrula
        cart_page.remove_item_from_cart()
        time.sleep(5)
        # **Sepetin boş olduğunu doğrula**
        assert cart_page.is_cart_empty(), "HATA: Ürün silinmedi, sepet hâlâ dolu!"

        # Ana sayfaya dön ve doğrula
        home_page.go_to_homepage()
        time.sleep(5)

        assert "Amazon" in driver.title, "HATA: Ana sayfaya dönülemedi!"


    except Exception as e:

        print(f"TEST BAŞARISIZ! Hata: {e}")

        # Screenshot Klasörünü Otomatik Kontrol Et

        screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Screenshot Kaydet (UUID ile benzersiz dosya adı)

        screenshot_filename = f"error_{uuid.uuid4().hex[:8]}.png"  # 8 karakterlik benzersiz ID

        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

        driver.save_screenshot(screenshot_path)

        print(f"Hata ekran görüntüsü alındı: {screenshot_path}")

        # Hata detaylarını raporlamak için fırlat

        raise

    finally:
        # Tarayıcıyı kapat
        time.sleep(5)
        driver.quit()
