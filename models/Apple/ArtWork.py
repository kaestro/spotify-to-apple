# models/AppleModels/ArtWork.py
from pydantic import BaseModel


class ColorScheme:
    def __init__(
        self,
        bgColor: str,
        textColor1: str,
        textColor2: str,
        textColor3: str,
        textColor4: str,
    ):
        self._bgColor = bgColor
        self._textColor1 = textColor1
        self._textColor2 = textColor2
        self._textColor3 = textColor3
        self._textColor4 = textColor4

    def get_bgColor(self):
        return self._bgColor

    def get_textColor1(self):
        return self._textColor1

    def get_textColor2(self):
        return self._textColor2

    def get_textColor3(self):
        return self._textColor3

    def get_textColor4(self):
        return self._textColor4


class ArtWork(BaseModel):
    def __init__(self, url: str, width: int, height: int, color_scheme: ColorScheme):
        self._url = url
        self._width = width
        self._height = height
        self._color_scheme = color_scheme

    def get_url(self):
        return self._url

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_color_scheme(self):
        return self._color_scheme
