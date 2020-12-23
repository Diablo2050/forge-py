import requests
import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
load_dotenv()
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
# ENV
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)