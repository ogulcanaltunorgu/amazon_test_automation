import time
from pages.home_page import HomePage  # HomePage sınıfı güncellenmiş olmalı!
from test.base_test import BaseTest


class TestCheckAddToCartAmazon(BaseTest):
    def test_check_amazon_add_to_cart(self):
        home_page = HomePage(self.driver)


        # 1. Anasayfada olduğumuzu doğrula
        self.assertEqual(self.base_url, home_page.get_current_url(), 'Amazon anasayfasında değilsin!')
        time.sleep(5)

        # 2. Arama yap ('samsung')
        home_page.search_product("samsung")
