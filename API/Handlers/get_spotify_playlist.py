# API/Routes/get_spotify_playlist.py
from fastapi import APIRouter, HTTPException
from API.Services import get_spotify_playlist_service
from models.Spotify.PlayListResponse import (
    response_json_to_playListResponse,
    PlayListResponse,
)

router = APIRouter()


@router.get("/spotify-playlist/{playlist_id}")
async def get_spotify_playlist(playlist_id: str):
    response = await get_spotify_playlist_service(playlist_id)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()
