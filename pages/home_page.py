from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    HOME_LOGO = (By.ID, "nav-logo")  # Amazon ana sayfa logosu

    def search_product(self, product_name):
        self.find(*self.SEARCH_BOX).send_keys(product_name)
        self.click_element(*self.SEARCH_BUTTON)

    def go_to_homepage(self):
        """Amazon logosuna tıklayarak anasayfaya dön."""
        try:
            home_logo = self.wait.until(EC.visibility_of_element_located(self.HOME_LOGO))  # Logonun görünmesini bekle
            self.driver.execute_script("arguments[0].scrollIntoView();", home_logo)  # Sayfayı logoya kaydır

            try:
                home_logo.click()  # Normal Selenium Click
            except:
                print("Normal click çalışmadı, JavaScript ile deniyoruz...")
                self.driver.execute_script("arguments[0].click();", home_logo)  # JavaScript ile tıkla

            self.wait.until(EC.title_contains("Amazon"))  # Sayfanın tamamen yüklenmesini bekle
            print("Başarıyla anasayfaya dönüldü!")

        except Exception as e:
            print(f"HATA: Ana sayfaya dönülemedi! -> {e}")