# models/Attributes.py
from click import DateTime
from pydantic import BaseModel

from models import PlayParams
from models.Apple.ArtWork import ArtWork
from models.Apple.Preview import Preview

from enums.GenreTypes import GenreType


class Attributes(BaseModel):
    pass


class TrackDetails:
    def __init__(
        self,
        url: str,
        name: str,
        artwork: ArtWork,
        previews: list[Preview],
        album_name: str,
        artist_name: str,
    ):
        self._url = url
        self._name = name
        self._artwork = artwork
        self._previews = previews
        self._album_name = album_name
        self._artist_name = artist_name

    def get_url(self):
        return self._url

    def get_name(self):
        return self._name

    def get_artwork(self):
        return self._artwork

    def get_previews(self):
        return self._previews

    def get_album_name(self):
        return self._album_name

    def get_artist_name(self):
        return self._artist_name


class TrackMetadata:
    def __init__(
        self,
        isrc: str,
        disc_number: int,
        genre_names: list[GenreType],
        play_params: PlayParams,
        release_date: DateTime,
        track_number: int,
        duration_in_millis: int,
    ):
        self._isrc = isrc
        self._disc_number = disc_number
        self._genre_names = genre_names
        self._play_params = play_params
        self._release_date = release_date
        self._track_number = track_number
        self._duration_in_millis = duration_in_millis

    def get_isrc(self):
        return self._isrc

    def get_disc_number(self):
        return self._disc_number

    def get_genre_names(self):
        return self._genre_names

    def get_play_params(self):
        return self._play_params

    def get_release_date(self):
        return self._release_date

    def get_track_number(self):
        return self._track_number

    def get_duration_in_millis(self):
        return self._duration_in_millis


class TrackExtras:
    def __init__(
        self, has_lyrics: bool, has_credits: bool, is_apple_digital_master: bool
    ):
        self._has_lyrics = has_lyrics
        self._has_credits = has_credits
        self._is_apple_digital_master = is_apple_digital_master

    def get_has_lyrics(self):
        return self._has_lyrics

    def get_has_credits(self):
        return self._has_credits

    def get_is_apple_digital_master(self):
        return self._is_apple_digital_master


class AppleAttributes(Attributes):
    def __init__(
        self, details: TrackDetails, metadata: TrackMetadata, extras: TrackExtras
    ):
        self._details = details
        self._metadata = metadata
        self._extras = extras

    def get_details(self):
        return self._details

    def get_metadata(self):
        return self._metadata

    def get_extras(self):
        return self._extras
