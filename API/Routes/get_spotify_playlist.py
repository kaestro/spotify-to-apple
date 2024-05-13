# API/Routes/get_spotify_playlist.py
from fastapi import APIRouter, HTTPException
import httpx
import os

router = APIRouter()


@router.get("/spotify-playlist/{playlist_id}")
async def get_spotify_playlist(playlist_id: str):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    token = os.getenv("SPOTIFY_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()
