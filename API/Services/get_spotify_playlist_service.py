import os

import httpx


async def get_spotify_playlist_service(playlist_id: str):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    token = os.getenv("SPOTIFY_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    return response
