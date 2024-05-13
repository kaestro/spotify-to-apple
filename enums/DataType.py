# enums/DataType.py
from enum import Enum


class DataType(Enum):
    ALBUM = "albums"
    ARTIST = "artists"
    PLAYLIST = "playlists"
    TRACK = "tracks"
