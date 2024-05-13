# model/Album.py
from click import DateTime
from pydantic import BaseModel

from models.Artist import Artist
from models.ExternalUrl import ExternalUrls
from models.Market import Market
from models.Image import Image

from enums.DatePrecision import DatePrecision
from enums.AlbumType import AlbumType


class Album(BaseModel):
    _id: str
    _uri: str
    _href: str
    _name: str
    _type: str
    _images: list[Image]
    _artists: list[Artist]
    _album_type: AlbumType
    _release_date: DateTime
    _total_tracks: int
    _external_urls: ExternalUrls
    _available_markets: list[Market]
    _release_date_precision: DatePrecision
