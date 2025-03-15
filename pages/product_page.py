from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    GO_TO_CART_BUTTON = (By.XPATH, "//span[@id='sw-gtc']//a")  # Sepete git butonu (Doğru XPath ile güncellendi)


    def add_to_cart(self):
        element = self.wait_element(self.ADD_TO_CART_BUTTON)  # Butonu bekle
        self.driver.execute_script("arguments[0].click();", element)  # JavaScript ile tıkla

    def go_to_cart(self):
        """Sepete git butonuna tıkla."""
        try:
            go_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.GO_TO_CART_BUTTON))  # Tıklanabilir olmasını bekle
            self.driver.execute_script("arguments[0].scrollIntoView();", go_to_cart_button)  # Butonu görünür yap
            self.driver.execute_script("arguments[0].click();", go_to_cart_button)  # JavaScript ile tıkla
        except Exception as e:
            print(f"HATA: 'Sepete Git' butonuna tıklanamadı! -> {e}")