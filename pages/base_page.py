from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """Web öğesini bulur ve döndürür."""
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
