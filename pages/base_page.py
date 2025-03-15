from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        """Her sayfa için temel sınıf. WebDriver ve bekleme nesnesini tanımlar."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        """Verilen locatora göre bir elementi bulur."""
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """Verilen locatora sahip bir elemente tıklar."""
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        """Şu anki sayfanın URL'ini döndürür."""
        return self.driver.current_url

    def wait_element(self, method, message=''):
        """Verilen metoda göre bir elementin tıklanabilir olmasını bekler."""
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def wait_for_visibility(self, locator, message=''):
        """Verilen locatora sahip elementin görünür olmasını bekler."""
        return self.wait.until(ec.visibility_of_element_located(locator), message)

    def get_text(self, locator):
        """Belirtilen locatordan metni alır."""
        return self.wait_for_visibility(locator).text

