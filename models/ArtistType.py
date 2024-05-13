# models/ArtistType.py
from enum import Enum


class ArtistType(Enum):
    ARTIST = "artist"
    GROUP = "group"
    UNKNOWN = "unknown"
