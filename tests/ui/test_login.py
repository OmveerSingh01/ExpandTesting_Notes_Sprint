import pytest
from config.env import ConfigReader
from pages.login_page import LoginPage
from time import sleep
from utils.screenshot import take_screenshot
from utils.loggers import get_logger
from utils.performance import get_page_load_time

logger = get_logger()

@pytest.mark.order(1)
@pytest.mark.ui
def test_invalid_login(setup_and_teardown):
    driver = setup_and_teardown
    logger.info("Starting test_invalid_login")
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

@pytest.mark.order(2)
@pytest.mark.ui
def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown
    logger.info("Starting test_valid_login")
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
    # Log Notes page load time
    load_time = get_page_load_time(driver)
    get_logger().info(f"Notes Page Load Time: {load_time} ms")

    assert driver.current_url =="https://practice.expandtesting.com/notes/app"