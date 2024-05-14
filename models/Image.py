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


def response_json_to_image(response_json: dict):
    return Image(
        response_json["url"],
        response_json["width"],
        response_json["height"],
    )
