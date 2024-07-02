from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from .page import Page

class OverviewPage(Page):
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        self.url = "https://demo.applitools.com/app.html"
        self.logged_user_name_div = (By.CLASS_NAME, 'logged-user-name')
        self.logged_user_role_div = (By.CLASS_NAME, 'logged-user-role')
        self.balance_value_div = (By.XPATH, '//div[@class="balance"]/div[@class="balance-value"]')

    def verify_balance_value(self, expected_balance_value: int):
        balance_value_element = self.driver.find_element(*self.balance_value_div)
        actual_balance_value = int("".join(re.findall(r"\d+", balance_value_element.text)))
        print(actual_balance_value, expected_balance_value)
        assert actual_balance_value == expected_balance_value
