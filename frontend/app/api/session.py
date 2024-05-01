
from .api import API    
from .constants import API_URL


class SessionAPI:
    URL = f"{API_URL}/sessions/"

    @staticmethod
    def create() -> str:
        response = API.post(SessionAPI.URL)

        session_id = response["id"]
        return session_id
