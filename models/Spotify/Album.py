# model/Album.py
from click import DateTime
from pydantic import BaseModel

from models.Market import Market
from models.Image import Image

from enums.DatePrecision import DatePrecision
from enums.AlbumType import AlbumType
from models.Spotify.Artist import Artist
from models.Spotify.ExternalUrl import ExternalUrls


class AlbumDetails:
    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        name: str,
        type: str,
        images: list[Image],
        artists: list[Artist],
    ):
        self._id = id
        self._uri = uri
        self._href = href
        self._name = name
        self._type = type
        self._images = images
        self._artists = artists

    def get_id(self):
        return self._id

    def get_uri(self):
        return self._uri

    def get_href(self):
        return self._href

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_images(self):
        return self._images

    def get_artists(self):
        return self._artists


class AlbumMetadata:
    def __init__(
        self,
        album_type: AlbumType,
        release_date: DateTime,
        total_tracks: int,
        external_urls: ExternalUrls,
        available_markets: list[Market],
        release_date_precision: DatePrecision,
    ):
        self._album_type = album_type
        self._release_date = release_date
        self._total_tracks = total_tracks
        self._external_urls = external_urls
        self._available_markets = available_markets
        self._release_date_precision = release_date_precision

    def get_album_type(self):
        return self._album_type

    def get_release_date(self):
        return self._release_date

    def get_total_tracks(self):
        return self._total_tracks

    def get_external_urls(self):
        return self._external_urls

    def get_available_markets(self):
        return self._available_markets

    def get_release_date_precision(self):
        return self._release_date_precision


class Album(BaseModel):
    def __init__(self, details: AlbumDetails, metadata: AlbumMetadata):
        self._details = details
        self._metadata = metadata

    def get_details(self):
        return self._details

    def get_metadata(self):
        return self._metadata
