# models/ArtWork.py
from pydantic import BaseModel


class ArtWork(BaseModel):
    _url: str
    _width: int
    _height: int
    _bgColor: str
    _textColor1: str
    _textColor2: str
    _textColor3: str
    _textColor4: str
