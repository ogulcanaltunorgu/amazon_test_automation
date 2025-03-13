import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.base_url) # Amazon açılacaktır.
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
