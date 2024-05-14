# models/Spotify/PlayListResponse.py
from pydantic import BaseModel

from models.Image import Image, response_json_to_image
from models.Spotify.ExternalUrl import ExternalUrls, response_json_to_external_urls
from models.Spotify.Followers import Followers, response_json_to_followers
from models.Spotify.PlayListOwner import PlayListOwner, response_json_to_play_list_owner
from typing import Union


class PlayListResponse(BaseModel):
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


def response_json_to_playListResponse(
    response_json: dict,
) -> Union[PlayListResponse, None]:
    try:
        return PlayListResponse(
            collaborative=response_json["collaborative"],
            description=response_json["description"],
            external_urls=response_json_to_external_urls(
                response_json["external_urls"]
            ),
            followers=response_json_to_followers(response_json["followers"]),
            id=response_json["id"],
            images=[response_json_to_image(image) for image in response_json["images"]],
            name=response_json["name"],
            owner=response_json_to_play_list_owner(response_json["owner"]),
            public=response_json["public"],
            snapshot_id=response_json["snapshot_id"],
        )
    except Exception as e:
        print(f"Failed to convert response to PlayListResponse: {e}")
        return None
