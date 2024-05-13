# models/Artists.py
from pydantic import BaseModel
from models.Spotify.ExternalUrl import ExternalUrls
from enums.ArtistType import ArtistType


class Artist(BaseModel):
    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        name: str,
        type: ArtistType,
        external_urls: ExternalUrls,
    ):
        self._id = id
        self._uri = uri
        self._href = href
        self._name = name
        self._type = type
        self._external_urls = external_urls

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

    def get_external_urls(self):
        return self._external_urls
