import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
api_model = os.getenv("GEMINI_API_MODEL")
api_url = os.getenv("GEMINI_API_URL")

if not all([api_key, api_model, api_url]):
    print("Missing required environment configuration: GEMINI_API_KEY, GEMINI_API_MODEL, GEMINI_API_URL")
    exit(1)

class Config:
    def __init__(self):
        self._key = api_key
        self._model = api_model
        self._url = api_url

    def get_key(self):
        return self._key

    def get_model(self):
        return self._model

    def get_url(self):
        return self._url
