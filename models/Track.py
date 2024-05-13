# model/Music.py
from pydantic import BaseModel

from models.DatePrecision import DatePrecision
from models.Market import Market
from models.ExternalUrl import ExternalUrls
from .Album import Album


class Track(BaseModel):
    id: str
    description: str


class AppleMusic(Track):
    _artist: str
    _album: str
    _track: str
    _duration: int
    _genre: str
    _release_date: str
    _artwork: str


class SpotifyMusic(Track):
    _id: str
    _uri: str
    _href: str
    _name: str
    _type: str
    _album: Album
    _artists: list[str]
    _explicit: bool
    _is_local: bool
    _popularity: int
    _disc_number: int
    _duration_ms: int
    _preview_url: str
    _external_ids: str
    _track_number: int
    _external_urls: ExternalUrls
    _available_markets: list[Market]
    _release_date_precision: DatePrecision
