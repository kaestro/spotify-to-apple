# Main.py
from fastapi import FastAPI
from API.Routes import get_spotify_playlist

app = FastAPI()

app.include_router(get_spotify_playlist.router)
