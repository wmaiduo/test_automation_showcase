from selenium import webdriver
from selenium.webdriver.common.by import By
from .page import Page

class LoginPage(Page):
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        self.url = "https://demo.applitools.com/"
        self.username_textbox = (By.ID, 'username')
        self.password_textbox = (By.ID, 'password')
        self.signin_button = (By.ID, 'log-in')
    
    def login(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.signin_button).click()