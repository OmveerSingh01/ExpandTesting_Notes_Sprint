from api.api_client import APIClient


class NotesAPI(APIClient):

    NOTES_ENDPOINT = "/notes"

    def get_all_notes(self, token):
        headers = {
            "x-auth-token": token
        }

        return self.get(
            endpoint=self.NOTES_ENDPOINT,
            headers=headers
        )

    def delete_note(self, note_id, token):
        headers = {
            "x-auth-token": token
        }

        return self.delete(
            endpoint=f"{self.NOTES_ENDPOINT}/{note_id}",
            headers=headers
        )

    def create_note(self,payload, token):
        headers = {
            "x-auth-token": token
        }
        return self.post(
            endpoint=self.NOTES_ENDPOINT,
            payload=payload,
            headers=headers
        )

    # def edit_note(self, note_id, payload, token):
    #     headers = {
    #         "x-auth-token": token
    #     }
    #     return self.put(
    #         endpoint=f"{self.NOTES_ENDPOINT}/{note_id}",
    #         payload=payload,
    #         headers=headers
    #     )

    def edit_note(self, note_id, payload, token):
        headers = {"x-auth-token": token}
        return self.put(
            endpoint=f"{self.NOTES_ENDPOINT}/{note_id}",
            payload=payload,
            headers=headers
        )