# models/Image.py
from pydantic import BaseModel


class Image(BaseModel):
    def __init__(self, url: str, width: int, height: int):
        self._url = url
        self._width = width
        self._height = height

    def get_url(self):
        return self._url

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
