# models/Artists.py
from pydantic import BaseModel
from .ExternalUrl import ExternalUrls
from .ArtistType import ArtistType


class Artist(BaseModel):
    _id: str
    _uri: str
    _href: str
    _name: str
    _type: ArtistType
    _external_urls: ExternalUrls
