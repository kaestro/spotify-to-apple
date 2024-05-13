# models/Preview.py
from pydantic import BaseModel


class Preview(BaseModel):

    def __init__(self, url: str):
        self._url = url

    def get_url(self):
        return self._url
