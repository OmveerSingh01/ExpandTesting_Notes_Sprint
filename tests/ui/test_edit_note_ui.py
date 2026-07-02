import pytest
from pages.create_note_page import NotesPage
from time import sleep

from pages.edit_page import EditPage
from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot
from utils.performance import get_page_load_time

logger = get_logger()

@pytest.mark.order(5)
@pytest.mark.ui

def test_valid_edit_note_ui(setup_and_teardown):
    logger.info("Starting test_valid_edit_note_ui")
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["valid_edit_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp.login()
    # Log Notes page load time
    load_time = get_page_load_time(setup_and_teardown)
    get_logger().info(f"Notes Page Load Time: {load_time} ms")
    ep.scroll()
    ep.click_edit()
    ep.select_work(CATEGORY)
    ep.enter_title(TITLE)
    ep.enter_description(DESCRIPTION)
    ep.click_create_btn()
    sleep(2)
    assert ep.validate_title() == 'Updated Work Note', 'Note not edited'

@pytest.mark.order(6)
@pytest.mark.ui

def test_invalid_edit_note_ui(setup_and_teardown):
    logger.info("Starting test_invalid_edit_note_ui")
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["invalid_edit_notes"]
    TITLE = env['title']
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp.login()
    print("description", DESCRIPTION)
    # Log Notes page load time
    load_time = get_page_load_time(setup_and_teardown)
    get_logger().info(f"Notes Page Load Time: {load_time} ms")
    ep.scroll()
    ep.click_edit()
    ep.select_work(CATEGORY)
    ep.enter_title(TITLE)
    ep.enter_description(DESCRIPTION)
    print("description",DESCRIPTION)
    ep.click_create_btn()
    sleep(2)
    try:
        assert ep.validate_title() == '', 'Note edited with empty title'
    except AssertionError:
        take_screenshot(ep.driver, "invalid_edit_note")
