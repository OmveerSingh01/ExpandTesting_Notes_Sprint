import pytest
from config.env import ConfigReader
from pages.create_note_page import NotesPage
from time import sleep
from pages.login_page import LoginPage
from pages.delete_page import DeletePage
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot
from utils.performance import get_page_load_time

logger = get_logger()

@pytest.mark.order(7)
@pytest.mark.ui
def test_delete_note_ui(setup_and_teardown):
    logger.info("Starting test_delete_note_ui")
    dp = DeletePage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)
    lp.login()
    # Log Notes page load time
    load_time = get_page_load_time(setup_and_teardown)
    get_logger().info(f"Notes Page Load Time: {load_time} ms")

    notes_before = len(dp.get_all_notes())
    dp.scroll()
    dp.click_delete()
    dp.click_confirm()
    sleep(2)
    notes_after = len(dp.get_all_notes())
    assert notes_after == notes_before - 1, "Note count did not decrease by 1 after deletion"






