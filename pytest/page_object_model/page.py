from selenium.webdriver.support.ui import WebDriverWait
from assertpy import assert_that

class Page:
    def open(self):
        self.driver.get(self.url)

    def verify_url(self):
        assert_that(self.driver.current_url).is_equal_to(self.url)

    def verify_element_displayed(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*by_locator))
        assert self.driver.find_element(*by_locator).is_displayed()