import pytest
from api.auth_api import AuthAPI
from api.notes_api import NotesAPI
from config.env import ConfigReader

config = ConfigReader.read_config()
BASE_URL = config["valid_user"]["api_base_url"]

def test_login_invalid_password():
    """FR-09: Invalid credentials should return 401"""
    auth = AuthAPI(BASE_URL)
    response = auth.login("wrong@email.com", "wrongpass")
    assert response.status_code == 401

def test_get_notes_without_token():
    """FR-09: Missing token should return 401"""
    notes = NotesAPI(BASE_URL)
    response = notes.get_all_notes(token="invalid_token_xyz")
    assert response.status_code == 401

def test_create_note_missing_title(api_client):
    """FR-09: Missing title should return 400"""
    token = api_client["token"]
    notes_api = api_client["notes_api"]
    payload = {"title": "", "description": "test", "category": "Work"}
    response = notes_api.create_note(payload, token)
    assert response.status_code == 400

def test_delete_nonexistent_note(api_client):
    """FR-09: Deleting fake note ID should return 400 or 404"""
    token = api_client["token"]
    notes_api = api_client["notes_api"]
    response = notes_api.delete_note("000000000000000000000000", token)
    assert response.status_code in [400, 404]