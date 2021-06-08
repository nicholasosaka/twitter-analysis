import os
from dotenv.main import load_dotenv
import os


class AppConfig:
    def __init__(self):
        self.config = load_dotenv()

    def get_api_key(self):
        return os.getenv("API_KEY")

    def get_api_secret_key(self):
        return os.getenv("API_SECRET_KEY")

    def get_bearer_token(self):
        return os.getenv("BEARER_TOKEN")

    def get_access_token(self):
        return os.getenv("ACCESS_TOKEN")

    def get_access_secret_token(self):
        return os.getenv("ACCESS_TOKEN_SECRET")
