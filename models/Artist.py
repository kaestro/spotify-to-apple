# models/Artists.py
from pydantic import BaseModel
from models.ExternalUrl import ExternalUrls
from enums.ArtistType import ArtistType


class Artist(BaseModel):
    _id: str
    _uri: str
    _href: str
    _name: str
    _type: ArtistType
    _external_urls: ExternalUrls
