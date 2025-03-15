from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SECOND_PAGE_LINK = (By.XPATH, "//a[contains(@class, 's-pagination-button') and contains(text(), '2')]")
    THIRD_PRODUCT_LINK = (By.XPATH, "(//div[@data-component-type='s-search-result'])[3]//a")  # 3. ürünün <a> etiketi

    def go_to_second_page(self):
        element = self.wait_element(self.SECOND_PAGE_LINK)  # Elementi bekle
        self.driver.execute_script("arguments[0].click();", element)  # JavaScript ile tıkla

    def go_to_third_product(self):
        product_element = self.wait_element(self.THIRD_PRODUCT_LINK)  # 3. ürünü bekle
        product_href = product_element.get_attribute("href")  # HREF'ini al
        self.driver.get(product_href)  # Direkt olarak ürüne git
