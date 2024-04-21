
import requests

from .contants import API_URL


class SessionAPI:
    URL = f"{API_URL}/sessions/"

    @staticmethod
    def create() -> str:
        # TODO: CHANGE USER ID
        response = requests.post(SessionAPI.URL, data={"user": "aa0eb13b-7044-4fde-923b-91acfe13fc6a"})

        session_id = response.json()["id"]
        return session_id
