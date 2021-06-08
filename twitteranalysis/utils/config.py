import os
from dotenv import dotenv_values


class AppConfig:
    def __init__(self, envfile):
        self.config = dotenv_values(envfile)

    def get_api_key(self):
        return self.config.get("API_KEY")

    def get_api_secret_key(self):
        return self.config.get("API_SECRET_KEY")

    def get_bearer_token(self):
        return self.config.get("BEARER_TOKEN")

    def get_access_token(self):
        return self.config.get("ACCESS_TOKEN")

    def get_access_secret_token(self):
        return self.config.get("ACCESS_TOKEN_SECRET")
