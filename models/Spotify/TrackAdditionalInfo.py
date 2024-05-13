from pydantic import BaseModel
from models.Market import Market
from models.Spotify.ExternalUrl import ExternalUrls
from enums.DatePrecision import DatePrecision


class TrackDetails:
    def __init__(
        self,
        popularity: int,
        preview_url: str,
        external_ids: str,
        external_urls: ExternalUrls,
        available_markets: list[Market],
    ):
        self._popularity = popularity
        self._preview_url = preview_url
        self._external_ids = external_ids
        self._external_urls = external_urls
        self._available_markets = available_markets

    def get_popularity(self):
        return self._popularity

    def get_preview_url(self):
        return self._preview_url

    def get_external_ids(self):
        return self._external_ids

    def get_external_urls(self):
        return self._external_urls

    def get_available_markets(self):
        return self._available_markets


class TrackMetadata:
    def __init__(
        self,
        disc_number: int,
        duration_ms: int,
        track_number: int,
        release_date_precision: DatePrecision,
    ):
        self._disc_number = disc_number
        self._duration_ms = duration_ms
        self._track_number = track_number
        self._release_date_precision = release_date_precision

    def get_disc_number(self):
        return self._disc_number

    def get_duration_ms(self):
        return self._duration_ms

    def get_track_number(self):
        return self._track_number

    def get_release_date_precision(self):
        return self._release_date_precision


class TrackAdditionalInfo(BaseModel):
    def __init__(self, details: TrackDetails, metadata: TrackMetadata):
        self._details = details
        self._metadata = metadata

    def get_details(self):
        return self._details

    def get_metadata(self):
        return self._metadata
