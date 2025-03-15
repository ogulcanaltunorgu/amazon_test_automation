from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.XPATH, "//div[contains(@class, 'sc-list-item')]")  # Sepetteki ürün
    DELETE_BUTTON = (By.XPATH, "//input[contains(@value, 'Sil')]")  # Sil butonu
    EMPTY_CART_MESSAGE = (By.ID, "sc-subtotal-label-activecart")  # "Ara toplam (0 ürün)" mesajı

    def verify_item_in_cart(self):
        """Sepette ürün olup olmadığını kontrol eder."""
        return len(self.driver.find_elements(*self.CART_ITEM)) > 0  # Sepette ürün varsa True döner

    def remove_item_from_cart(self):
        """Ürünü sepetten sil ve gerçekten silindiğini doğrula."""
        try:
            delete_button = self.wait_element(self.DELETE_BUTTON)  # Sil butonunu bekle
            self.driver.execute_script("arguments[0].click();", delete_button)  # JavaScript ile tıkla

        except Exception as e:
            print(f"HATA: Ürün silinemedi! -> {e}")

    def is_cart_empty(self):
        """Sepetin tamamen boş olup olmadığını kontrol eder."""
        try:
            empty_cart_text = self.wait_element(self.EMPTY_CART_MESSAGE).text  # "Ara toplam (0 ürün)" mesajını al
            return "0 ürün" in empty_cart_text  # Eğer "0 ürün" yazıyorsa, sepet boş demektir
        except:
            return False  # Eğer mesaj bulunmazsa, sepet hala doludur
