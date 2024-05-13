from pydantic import BaseModel
from enums.TrackType import TrackType


class Track(BaseModel):
    _id: str
    _href: str
    _type: TrackType

    def __init__(self, id: str, href: str, type: TrackType):
        self._id = id
        self._href = href
        self._type = type
