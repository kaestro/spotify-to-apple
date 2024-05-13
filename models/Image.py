# models/Image.py
from pydantic import BaseModel


class Image(BaseModel):
    _url: str
    _width: int
    _height: int
