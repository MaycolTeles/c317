
from .api import API
from .contants import API_URL


class UserMessageAPI:
    URL = f"{API_URL}/user-messages/"

    @staticmethod
    def create(message: str, session_id: str) -> None:
        body = {
            "content": message,
            "user": "aa0eb13b-7044-4fde-923b-91acfe13fc6a",
            "session": session_id,
        }
        response = API.post(UserMessageAPI.URL, body=body)

        print("RESPONSE: ", response)
