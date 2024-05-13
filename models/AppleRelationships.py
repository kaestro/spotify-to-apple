# models/AppleRelationships.py
from pydantic import BaseModel

from models.AppleData import AppleAlbumData, AppleArtistData


class Href(BaseModel):
    def __init__(self, _value: str):
        self._value = _value

    def __str__(self):
        return self._value

    def getValue(self):
        return self._value


class AppleRelationships(BaseModel):
    def __init__(
        self,
        _albums: tuple[list[AppleAlbumData], Href],
        _artists: tuple[list[AppleArtistData], Href],
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
