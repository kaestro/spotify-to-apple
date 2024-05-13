from pydantic import BaseModel
from models.Spotify.Album import Album


class TrackBasicInfo(BaseModel):

    def __init__(
        self,
        uri: str,
        name: str,
        album: Album,
        artists: list[str],
        explicit: bool,
        is_local: bool,
    ):
        self._uri = uri
        self._name = name
        self._album = album
        self._artists = artists
        self._explicit = explicit
        self._is_local = is_local

    def get_uri(self):
        return self._uri

    def get_name(self):
        return self._name

    def get_album(self):
        return self._album

    def get_artists(self):
        return self._artists

    def get_explicit(self):
        return self._explicit

    def get_is_local(self):
        return self._is_local

    def __str__(self):
        return f"SpotifyTrackBasicInfo(uri={self._uri}, name={self._name}, album={self._album}, artists={self._artists}, explicit={self._explicit}, is_local={self._is_local})"
