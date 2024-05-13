# models/PlayList.py
from pydantic import BaseModel

from models.Market import Market


class Playlist(BaseModel):
    pass


class SpotifyPlayList(Playlist):

    def __init__(self):
        playlist_id: str
        market: Market
        fields: list[str]
        additional_types: list[str]
