import pytest
from config.env import ConfigReader
from pages.create_note_page import NotesPage
from time import sleep
from pages.login_page import LoginPage
from pages.delete_page import DeletePage
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot

def test_delete_note_ui(setup_and_teardown):
    dp = DeletePage(setup_and_teardown)
    cp = LoginPage(setup_and_teardown)
    cp.login()
    sleep(2)
    dp.scroll()
    dp.click_delete()
    sleep(1)
    dp.click_confirm()






