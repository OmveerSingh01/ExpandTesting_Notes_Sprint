# import pytest
#
# # from config.config_reader import ConfigReader
# # from pages.notes_page import NotesPage
#
# from api.api_client import APIClient
# from api.notes_api import NotesAPI
#
#
# @pytest.mark.api
# @pytest.mark.order(5)
# def test_delete_note_api_ui(
#         browser,
#         api_client
# ):
#     token = api_client['token']
#
#     notes_api = NotesAPI(api_client)
#     response = notes_api.get_all_notes(token)
#     response_json = response.json()
#
