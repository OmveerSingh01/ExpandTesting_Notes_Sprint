from selenium.webdriver.common.by import By
from time import sleep
from config.env import ConfigReader
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_btn = (By.XPATH, "//a[.='Login']")
    email_btn = (By.ID, "email")
    password_btn = (By.ID, "password")
    submit_btn = (By.XPATH, '//button[@type="submit"]')

    def __init__(self,driver):
        super().__init__(driver)

    def click_login(self):
        self.click(self.login_btn)

    def click_email(self):
        self.click(self.email_btn)

    def enter_email(self,text):
        self.enter_text(self.email_btn,text)

    def click_password(self):
        self.click(self.password_btn)

    def enter_password(self,text):
        self.enter_text(self.password_btn,text)

    def click_submit(self):
        self.click(self.submit_btn)

    def login(self):
        config = ConfigReader.read_config()
        env = config["valid_user"]
        USERNAME = env["username"]
        PASSWORD = env["password"]

        self.scroll()
        self.click_login()
        sleep(2)
        self.scroll()
        self.click_email()
        self.enter_email(USERNAME)
        self.click_password()
        self.enter_password(PASSWORD)
        self.click_submit()
        sleep(2)

