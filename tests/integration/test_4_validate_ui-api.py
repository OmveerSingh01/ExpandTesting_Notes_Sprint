from http.client import responses
from time import sleep

from config.env import ConfigReader
import pytest
from pages.create_note_page import NotesPage

from api.notes_api import NotesAPI
from pages.login_page import LoginPage

@pytest.mark.integration
@pytest.mark.order(15)
def test_validate_note(setup_and_teardown,api_client):
    config = ConfigReader.read_config()
    note_data = config["valid_notes"]

    expected_title = note_data["title"]
    expected_description = note_data["description"]
    expected_category = note_data["category"]

    lp = LoginPage(setup_and_teardown)
    np = NotesPage(setup_and_teardown)

    lp.login()
    np.scroll()
    np.click_add_btn()
    np.select_work(expected_category)
    np.enter_title_btn(expected_title)
    np.click_description_btn()
    np.enter_description_btn(expected_description)
    np.click_create_btn()

    sleep(2)

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    response = notes_api.get_all_notes(token)
    assert response.status_code == 200

    notes = response.json()["data"]

    matched_note = None

    for i in notes:
        if i["title"] == expected_title and i["description"] == expected_description:
            matched_note = True
            assert matched_note == True
            break
    assert matched_note == True, "Note not found in API response"

