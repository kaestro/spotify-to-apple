# models/Spotify/PlayListResponse.py
from pydantic import BaseModel

from models.Image import Image
from models.Spotify.ExternalUrl import ExternalUrls
from models.Spotify.Followers import Followers
from models.Spotify.PlayListOwner import PlayListOwner
from models.Spotify.Track import Track


class PlaylistResponse(BaseModel):
    def __init__(
        self,
        collaborative: bool,
        description: str,
        external_urls: ExternalUrls,
        followers: Followers,
        id: str,
        images: list[Image],
        name: str,
        owner: PlayListOwner,
        public: bool,
        snapshot_id: str,
    ):
        self._collaborative = collaborative
        self._description = description
        self._external_urls = external_urls
        self._followers = followers
        self._id = id
        self._images = images
        self._name = name
        self._owner = owner
        self._public = public
        self._snapshot_id = snapshot_id

    @property
    def collaborative(self):
        return self._collaborative

    @property
    def description(self):
        return self._description

    @property
    def external_urls(self):
        return self._external_urls

    @property
    def followers(self):
        return self._followers

    @property
    def id(self):
        return self._id

    @property
    def images(self):
        return self._images

    @property
    def name(self):
        return self._name

    @property
    def owner(self):
        return self._owner

    @property
    def public(self):
        return self._public

    @property
    def snapshot_id(self):
        return self._snapshot_id
