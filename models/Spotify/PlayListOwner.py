# models/Spotify/PlayListOwner.py
from pydantic import BaseModel

from enums.OwnerType import OwnerType
from models.Spotify.ExternalUrl import ExternalUrls, response_json_to_external_urls
from models.Spotify.Followers import Followers, response_json_to_followers


class PlayListOwner(BaseModel):
    def __init__(
        self,
        external_urls: ExternalUrls,
        followers: Followers,
        href: str,
        id: str,
        uri: str,
        display_name: str,
        type: OwnerType = OwnerType.USER,
    ):
        self._external_urls = external_urls
        self._followers = followers
        self._href = href
        self._id = id
        self._type = type
        self._uri = uri
        self._display_name = display_name

    @property
    def external_urls(self):
        return self._external_urls

    @property
    def followers(self):
        return self._followers

    @property
    def href(self):
        return self._href

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def uri(self):
        return self._uri

    @property
    def display_name(self):
        return self._display_name


def response_json_to_play_list_owner(response_json: dict):
    return PlayListOwner(
        external_urls=response_json_to_external_urls(response_json["external_urls"]),
        followers=response_json_to_followers(response_json["followers"]),
        href=response_json["href"],
        id=response_json["id"],
        uri=response_json["uri"],
        display_name=response_json["display_name"],
    )
