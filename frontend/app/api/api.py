
import os
from typing import Any

import requests


class API:

    @staticmethod
    def get(url: str, body: dict[str, Any] = {}) -> dict[str, Any]:
        headers = API.get_headers()
        response = requests.get(url, data=body, headers=headers)
        response.raise_for_status()

        return response.json()

    @staticmethod
    def post(url: str, body: dict[str, Any] = {}) -> dict[str, Any]:
        headers = API.get_headers()
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()

        return response.json()
    
    @staticmethod
    def put(url: str, body: dict[str, Any] = {}) -> dict[str, Any]:
        headers = API.get_headers()
        response = requests.put(url, data=body, headers=headers)
        response.raise_for_status()

        return response.json()
    
    @staticmethod
    def delete(url: str, body: dict[str, Any] = {}) -> dict[str, Any]:
        headers = API.get_headers()
        response = requests.delete(url, data=body, headers=headers)
        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_headers():
        token = os.environ.get("token")
        return {
            "Authorization": f"Token {token}"
        }
