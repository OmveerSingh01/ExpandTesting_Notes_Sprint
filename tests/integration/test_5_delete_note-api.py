from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.create_note_page import NotesPage
from pages.base_page import BasePage
from time import sleep
from utils.loggers import get_logger
from utils.performance import get_page_load_time
import pytest
logger = get_logger()

@pytest.mark.integration
@pytest.mark.order(16)
def test_delete_and_validate(setup_and_teardown, api_client):
    """FR-06 + FR-07: API delete must reflect on UI"""
    driver = setup_and_teardown
    token = api_client["token"]
    notes_api = api_client["notes_api"]

    # Fresh note create
    config = ConfigReader.read_config()["valid_notes"]
    payload = {
        "title": config["title"],
        "description": config["description"],
        "category": config["category"]
    }
    create_resp = notes_api.create_note(payload, token)
    assert create_resp.status_code == 200
    note_id = create_resp.json()["data"]["id"]
    note_title = create_resp.json()["data"]["title"]
    logger.info(f"Created note with ID: {note_id}, Title: {note_title}")

    # Delete via API
    delete_resp = notes_api.delete_note(note_id, token)
    assert delete_resp.status_code in (200, 204)
    logger.info(f"Deleted note with ID: {note_id}, Title: {note_title}")

    # API verify
    remaining = notes_api.get_all_notes(token).json()["data"]
    assert note_id not in [n["id"] for n in remaining], "Note still in API"

    # UI verify
    lp = LoginPage(driver)
    lp.login()
    BasePage(driver).refresh()
    sleep(3)

    # Log Notes page load time after refresh
    load_time = get_page_load_time(driver)
    logger.info(f"Notes Page Load Time: {load_time} ms")

    note_cards = driver.find_elements("xpath", '//span[@data-testid="note-card-title"]')
    ui_titles = [card.text for card in note_cards]
    assert note_title not in ui_titles, "Note still visible in UI"
    logger.info("Note disappeared from UI after deletion via API")