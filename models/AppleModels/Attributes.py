# models/Attributes.py
from click import DateTime
from pydantic import BaseModel

from models import PlayParams
from models.ArtWork import ArtWork
from models.Preview import Preview

from enums.GenreTypes import GenreType


class Attributes(BaseModel):
    pass


class AppleAttributes(Attributes):
    _url: str
    _isrc: str
    _name: str
    _artwork: ArtWork
    _previews: list[Preview]
    _album_name: str
    _has_lyrics: bool
    _artist_name: str
    _disc_number: int
    _genre_names: list[GenreType]
    _has_credits: bool
    _play_params: PlayParams
    _release_date: DateTime
    _track_number: int
    _duration_in_millis: int
    _is_apple_digital_master: bool
