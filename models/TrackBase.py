from pydantic import BaseModel
from enums.TrackType import TrackType


class TrackBase(BaseModel):

    def __init__(self, id: str, href: str, type: TrackType):
        self._id = id
        self._href = href
        self._type = type
