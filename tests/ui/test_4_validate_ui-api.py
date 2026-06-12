from http.client import responses
from config.env import ConfigReader
import pytest
from pages.create_note_page import NotesPage
from api.notes_api import NotesAPI

def test_validate_note(api_client):
    config = ConfigReader.read_config()
    note_data = config["valid_notes"]

    expected_title = note_data["title"]
    expected_description = note_data["description"]

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