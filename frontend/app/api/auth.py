
import os

import requests

from .contants import API_AUTH_URL


class AuthAPI:
    URL = f"{API_AUTH_URL}"

    @staticmethod
    def register_user(username: str, email: str, password: str) -> tuple[str, str]:
        body = {
            "name": username,
            "email": email,
            "password": password,
        }
        url = f"{AuthAPI.URL}/register/"
        response = requests.post(url, data=body)
        response.raise_for_status()

        user_id = response.json()["user"]["id"]
        token = response.json()["token"]

        os.environ["token"] = token

        return user_id, token

    @staticmethod
    def login_user(email: str, password: str) -> str:
        body = {
            "email": email,
            "password": password,
        }
        url = f"{AuthAPI.URL}/login/"
        response = requests.post(url, data=body)
        response.raise_for_status()

        token = response.json()["token"]

        os.environ["token"] = token

        return token

    @staticmethod
    def update_password(email: str, password: str) -> None:
        body = {
            "email": email,
            "password": password,
        }
        url = f"{AuthAPI.URL}/reset-password/"
        response = requests.post(url, data=body)
        response.raise_for_status()
