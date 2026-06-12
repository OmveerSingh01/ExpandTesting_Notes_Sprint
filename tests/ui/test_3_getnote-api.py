import pytest
import time


@pytest.mark.api
def test_get_all_notes(api_client):

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    start_time = time.time()

    response = notes_api.get_all_notes(token)

    response_time = time.time() - start_time

    # Validate status code
    assert response.status_code == 200

    response_json = response.json()

    # Validate notes list
    assert "data" in response_json
    assert isinstance(response_json["data"], list)

    # Validate response time
    assert response_time < 2, \
        f"Response time exceeded: {response_time:.2f} sec"