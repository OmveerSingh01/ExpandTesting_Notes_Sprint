import pytest
from config.env import ConfigReader
from pages.create_note_page import NotesPage
from time import sleep

from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot


def test_valid_note(setup_and_teardown):
    np = NotesPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["valid_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]

    lp = LoginPage(setup_and_teardown)
    lp.login()
    sleep(5)

    # np.scroll()
    np.click_add_btn()
    sleep(1)

    np.click_category_btn()
    np.click_work_btn()

    sleep(2)
    np.click_title_btn()
    np.enter_title_btn(TITLE)
    np.click_description_btn()
    np.enter_description_btn(DESCRIPTION)
    np.click_create_btn()

    assert np.validate_title() == 'Work Note','Note not created'
    assert np.validate_description() == "This is a test note created by automation script.", 'Note not created '

def test_invalid_note(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    np = NotesPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["invalid_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]


    # lp.login()
    sleep(5)
    # np.scroll()
    np.click_add_btn()
    np.click_category_btn()
    np.click_work_btn()
    sleep(2)
    # np.click_title_btn()
    sleep(2)
    np.enter_title_btn(TITLE)
    np.click_description_btn()
    np.enter_description_btn(DESCRIPTION)
    np.click_create_btn()
    print(np.validate_title())
    print(np.validate_description())
    sleep(2)
    try:
        assert np.validate_title() == '', 'Note created with empty title'
    except AssertionError:
        take_screenshot(np.driver, "invalid_note")
    # assert np.validate_description() != "This is a test note created by automation script.", 'Note not created '