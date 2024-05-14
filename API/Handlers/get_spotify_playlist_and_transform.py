# API/Routes/get_spotify_playlist_and_transform.py
from fastapi import APIRouter, HTTPException
from models.Spotify.PlayListResponse import (
    response_json_to_playListResponse,
    PlayListResponse,
)
from Services.get_spotify_playlist_service import get_spotify_playlist_service

router = APIRouter()


# TODO: response로 받은 값을 service에서 저장한다.
@router.get("/transform-spotify-playlist/{playlist_id}")
async def get_spotify_playlist_and_transform(playlist_id: str):
    response = await get_spotify_playlist_service(playlist_id)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    playListResponse: PlayListResponse = response_json_to_playListResponse(
        response.json()
    )

    if playListResponse is None:
        raise HTTPException(
            status_code=500, detail="Failed to transform response to PlayListResponse"
        )

    return response.json()
