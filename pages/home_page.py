import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".s-main-slot")
    PAGE_NUMBER = (By.CSS_SELECTOR, ".s-pagination-item.s-pagination-selected")

    def search_product(self, product_name):
        """Ürün arama işlemini gerçekleştirir."""
        search_box = self.find_element(self.SEARCH_BOX) # Arama kutusunu bul
        search_box.clear() # Arama kutusundaki eski veriyi temizle
        search_box.send_keys(product_name) # Bizim son arama verimizi gir
        #search_box.send_keys(Keys.RETURN)

        #Enter tuşu ile çalışmayan bir JavaScript tetikleyici varsa, arama butonuna basılması gerekebilirdi.
        # Bu sebepten aşağıdaki gibi de yapılabilir. :)
        search_button = self.find_element(self.SEARCH_BUTTON)
        search_button.click()
