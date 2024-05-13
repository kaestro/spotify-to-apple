# models/PlayList.py
from pydantic import BaseModel
from models.Market import Market


class Playlist(BaseModel):
    pass


class SpotifyPlayList(Playlist):
    def __init__(
        self,
        playlist_id: str,
        market: Market,
        fields: list[str],
        additional_types: list[str],
    ):
        self._playlist_id = playlist_id
        self._market = market
        self._fields = fields
        self._additional_types = additional_types

    @property
    def playlist_id(self):
        return self._playlist_id

    @property
    def market(self):
        return self._market

    @property
    def fields(self):
        return self._fields

    @property
    def additional_types(self):
        return self._additional_types
