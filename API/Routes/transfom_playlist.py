from fastapi import FastAPI
from pydantic import BaseModel

# Pydantic model

app = FastAPI()

# @app.post("/transform")
# async def transform_playlist(playlist: Playlist):
# Transform the data as needed
# For example, let's just return the data as is
#     return playlist
