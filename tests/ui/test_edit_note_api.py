from config.env import ConfigReader


def test_edit_note(api_client):
    """Edit a note via API and verify updated values"""
    token = api_client["token"]
    notes_api = api_client["notes_api"]

    # Step 1: Get existing notes, pick first one
    response = notes_api.get_all_notes(token)
    assert response.status_code == 200

    notes = response.json()["data"]
    assert len(notes) > 0, "No notes found to edit"
    note_id = notes[0]["id"]

    # Step 2: Edit the note with config data
    config = ConfigReader.read_config()
    payload = config["valid_edit_notes"]

    edit_response = notes_api.edit_note(note_id, payload, token)
    print(edit_response.json())  # ← yeh add kar
    assert edit_response.status_code == 200

    # Step 3: Verify updated values in API response
    updated_note = edit_response.json()["data"]
    assert updated_note["title"] == payload["title"]
    assert updated_note["description"] == payload["description"]