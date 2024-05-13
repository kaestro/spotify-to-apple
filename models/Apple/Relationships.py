# models/AppleRelationships.py
from pydantic import BaseModel

from models.Apple.Data import Album, Artist


class Href(BaseModel):
    def __init__(self, _value: str):
        self._value = _value

    def __str__(self):
        return self._value

    def getValue(self):
        return self._value


class Relationships(BaseModel):
    def __init__(
        self,
        _albums: tuple[list[Album], Href],
        _artists: tuple[list[Artist], Href],
    ):
        self._albums = _albums
        self._artists = _artists

    def getAlbumsData(self):
        return self._albums[0]

    def getAlbumsHref(self):
        return self._albums[1]

    def getArtistsData(self):
        return self._artists[0]

    def getArtistsHref(self):
        return self._artists[1]
