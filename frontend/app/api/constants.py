
import os

import dotenv


dotenv.load_dotenv()


URL = os.getenv("API_URL", "http://localhost:8000")

API_URL = f"{URL}/api"

API_AUTH_URL = f"{URL}/auth"

WEBSOCKET_URL = os.getenv("WEBSOCKET_URL", "ws://localhost:8000")
