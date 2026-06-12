import pytest
from pages.create_note_page import NotesPage
from time import sleep

from pages.edit_page import EditPage
from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot

def test_valid_edit_note_ui(setup_and_teardown):
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["valid_edit_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp.login()
    sleep(2)
    ep.scroll()
    ep.click_edit()
    ep.enter_category()
    ep.click_personal()
    ep.enter_title(TITLE)
    ep.enter_description(DESCRIPTION)
    sleep(10)
    ep.click_create_btn()
    sleep(5)
    assert ep.validate_title() == 'Updated Work Note', 'Note not edited'

def test_invalid_edit_note_ui(setup_and_teardown):
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["invalid_edit_notes"]
    TITLE = ''
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp.login()
    sleep(2)
    ep.scroll()
    ep.click_edit()
    ep.enter_category()
    ep.click_personal()
    ep.enter_title(TITLE)
    ep.enter_description(DESCRIPTION)
    sleep(10)
    ep.click_create_btn()
    sleep(3)
    try:
        assert ep.validate_title() == '', 'Note edited with empty title'
    except AssertionError:
        take_screenshot(ep.driver, "invalid_edit_note")
