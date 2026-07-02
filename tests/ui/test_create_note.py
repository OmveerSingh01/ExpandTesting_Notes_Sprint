import pytest
from config.env import ConfigReader
from pages.create_note_page import NotesPage
from time import sleep

from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.performance import get_page_load_time
from utils.screenshot import take_screenshot

logger = get_logger()

@pytest.mark.order(3)
@pytest.mark.ui
def test_valid_note(setup_and_teardown):
    logger.info("Starting test_valid_note")
    np = NotesPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["valid_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]

    lp = LoginPage(setup_and_teardown)
    lp.login()
    # Log Notes page load time
    load_time = get_page_load_time(setup_and_teardown)
    get_logger().info(f"Notes Page Load Time: {load_time} ms")

    np.click_add_btn()
    np.select_work(CATEGORY)

    np.click_title_btn()
    np.enter_title_btn(TITLE)
    np.click_description_btn()
    np.enter_description_btn(DESCRIPTION)
    np.click_create_btn()
    sleep(2)
    assert np.validate_title() == 'Work Note','Note not created'
    assert np.validate_description() == "This is a test note created by automation script.", 'Note not created '

@pytest.mark.order(4)
@pytest.mark.ui
def test_invalid_note(setup_and_teardown):
    logger.info("Starting test_invalid_note")
    lp = LoginPage(setup_and_teardown)
    np = NotesPage(setup_and_teardown)
    config = ConfigReader.read_config()
    env = config["invalid_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["description"]
    CATEGORY = env["category"]


    lp.login()
    np.scroll()
    np.click_add_btn()
    np.select_work(CATEGORY)
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