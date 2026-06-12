import pytest
from pages.create_note_page import NotesPage
from time import sleep

from pages.edit_page import EditPage
from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot

def test_delete_note_ui(setup_and_teardown):
    dp = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["edit_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp.login()
    sleep(2)
    dp.scroll()
    dp.click_edit()
    dp.enter_category()
    dp.click_personal()
    dp.enter_title(TITLE)
    dp.enter_description(DESCRIPTION)
    sleep(10)
    dp.click_create_btn()