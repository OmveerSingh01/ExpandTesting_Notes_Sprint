import pytest

from config.env import ConfigReader
from utils.loggers import get_logger

logger = get_logger()

@pytest.mark.order(8)
@pytest.mark.api
def test_create_note(api_client):
    logger.info("Starting test_create_note")
    config = ConfigReader.read_config()
    note_data = config["valid_notes"]

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    payload = {
        "title": note_data["title"],
        "description": note_data["description"],
        "category": note_data["category"]
    }

    response = notes_api.create_note(payload,token)

    assert response.status_code == 200

    response_data = response.json()["data"]

    assert response_data["title"] == payload["title"]
    assert response_data["description"] == payload["description"]
    assert response_data["category"] == payload["category"]

    logger.info(f"Note created with title: {response_data['title']}")
