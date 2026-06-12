import pytest
from config.env import ConfigReader
from pages.login_page import LoginPage
from time import sleep
from utils.screenshot import take_screenshot
from utils.loggers import get_logger


def test_invalid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)
    config = ConfigReader.read_config()
    env = config["invalid_user"]
    USERNAME = env["username"]
    PASSWORD = env["password"]

    lp.scroll()
    lp.click_login()
    lp.scroll()
    lp.click_email()
    lp.enter_email(USERNAME)
    lp.click_password()
    lp.enter_password(PASSWORD)
    lp.click_submit()
    sleep(2)
    take_screenshot(driver, "invalid_login")
    sleep(2)
    assert driver.current_url != "https://practice.expandtesting.com/notes/app"
    # lp.refresh()


def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)
    config = ConfigReader.read_config()
    env = config["valid_user"]
    USERNAME = env["username"]
    PASSWORD = env["password"]
    get_logger().info("Trying to log in")
    lp.scroll()
    lp.click_login()
    lp.scroll()
    lp.click_email()
    lp.enter_email(USERNAME)
    lp.click_password()
    lp.enter_password(PASSWORD)
    lp.click_submit()
    sleep(2)
    assert driver.current_url =="https://practice.expandtesting.com/notes/app"