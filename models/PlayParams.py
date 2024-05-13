# models/PlayParams.py
from pydantic import BaseModel

from enums.TrackType import TrackType


class PlayParams(BaseModel):

    def __init__(self, id: str, kind: TrackType):
        self._id = id
        self._kind = kind
