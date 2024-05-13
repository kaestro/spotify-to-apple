# model/Music.py
from click import DateTime
from pydantic import BaseModel

from models.Attributes import Attributes
from models.Equivalent import Equivalent
from models.Market import Market
from models.ExternalUrl import ExternalUrls
from models.Album import Album

from enums.DatePrecision import DatePrecision
from enums.TrackType import TrackType


class Track(BaseModel):
    _id: str


class AppleMusicTrack(Track):
    _id: str
    _apple_music_id: int
    _href: str
    _type: TrackType

    _attributes: Attributes.AppleAttributes

    _equivalents: list[Equivalent]

    def _set_id(self):
        self._id = str(self._apple_music_id)

    def set_apple_music_id(self, apple_music_id: int):
        self._apple_music_id = apple_music_id
        self._set_id()


class SpotifyTrack(Track):
    _id: str
    _uri: str
    _href: str
    _name: str
    _type: TrackType
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
