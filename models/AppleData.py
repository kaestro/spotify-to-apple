from pydantic import BaseModel

from enums.DataType import DataType


class AppleData(BaseModel):
    _id: int
    _href: str
    _type: DataType

    def __init__(self, _id: int, _href: str, _type: DataType):
        self._id = _id
        self._href = _href
        self._type = _type


class AppleAlbumData(AppleData):

    def __init__(self, _id: int, _href: str):
        super().__init__(_id, _href, DataType.ALBUM)


class AppleArtistData(AppleData):

    def __init__(self, _id: int, _href: str):
        super().__init__(_id, _href, DataType.ARTIST)
