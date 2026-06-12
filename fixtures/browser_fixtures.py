import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from config.env import ConfigReader

@pytest.fixture(scope="function")
def setup_and_teardown():

    config = ConfigReader.read_config()
    env = config['qa']
    base_url = env['base_url']

    o = ChromeOptions()
    o.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.get(base_url)

    yield driver

    driver.quit()