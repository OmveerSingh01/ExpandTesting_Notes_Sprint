# import pytest
# from time import sleep
#
# from pages.base_page import BasePage
# from pages.login_page import LoginPage
# from pages.create_note_page import NotesPage
#
#
# @pytest.mark.integration
# @pytest.mark.order(12)
# def test_delete_and_validate(setup_and_teardown, api_client):
#     driver = setup_and_teardown
#     token = api_client["token"]
#     notes_api = api_client["notes_api"]
#
#     # Get all notes and store the note to be deleted
#     response = notes_api.get_all_notes(token)
#     assert response.status_code == 200, f"Failed to fetch notes. Status code: {response.status_code}"
#
#     response_json = response.json()
#     notes = response_json["data"]
#     assert len(notes) > 0, "No notes available to delete"
#
#     # Store the note details to be deleted (both title and description to handle duplicates)
#     note_to_delete = notes[0]
#     note_id = note_to_delete["id"]
#     note_title = note_to_delete["title"]
#     note_description = note_to_delete.get("description", "")
#
#     # Count occurrences of this (title, description) pair in API before deletion
#     api_count_before = sum(1 for n in notes if n.get("title") == note_title and n.get("description", "") == note_description)
#
#     # Login to access UI
#     lp = LoginPage(driver)
#     lp.login()
#     # sleep(2)
#
#     # Count occurrences of (title, description) pair in UI before deletion
#     cn = NotesPage(driver)
#     ui_count_before = cn.count_note_by_title_desc(note_title, note_description)
#
#     # Delete the note via API
#     delete_response = notes_api.delete_note(note_id, token)
#     assert delete_response.status_code in (200, 204), f"Failed to delete note. Status code: {delete_response.status_code}"
#
#     # Verify deletion via API - count should decrease by 1
#     remaining_notes = notes_api.get_all_notes(token)
#     remaining_notes_json = remaining_notes.json()["data"]
#     api_count_after = sum(1 for n in remaining_notes_json if n.get("title") == note_title and n.get("description", "") == note_description)
#
#     assert api_count_after == api_count_before - 1, \
#         f"API: Note (title='{note_title}', desc='{note_description}') count did not decrease by 1. Before: {api_count_before}, After: {api_count_after}"
#
#     # Refresh UI to get latest data
#     bp = BasePage(driver)
#     bp.refresh()
#     sleep(5)
#
#     # Verify deletion in UI - count should decrease by 1
#     ui_count_after = cn.count_note_by_title_desc(note_title, note_description)
#
#     assert ui_count_after == ui_count_before - 1, \
#         f"UI: Note (title='{note_title}', desc='{note_description}') count did not decrease by 1. Before: {ui_count_before}, After: {ui_count_after}"


from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.create_note_page import NotesPage
from pages.base_page import BasePage
from time import sleep
import pytest

@pytest.mark.integration
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

    # Delete via API
    delete_resp = notes_api.delete_note(note_id, token)
    assert delete_resp.status_code in (200, 204)

    # API verify
    remaining = notes_api.get_all_notes(token).json()["data"]
    assert note_id not in [n["id"] for n in remaining], "Note still in API"

    # UI verify
    lp = LoginPage(driver)
    lp.login()
    BasePage(driver).refresh()
    sleep(3)

    note_cards = driver.find_elements("xpath", '//span[@data-testid="note-card-title"]')
    ui_titles = [card.text for card in note_cards]
    assert note_title not in ui_titles, "Note still visible in UI"