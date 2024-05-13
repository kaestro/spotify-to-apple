from pydantic import BaseModel

from enums.DataType import DataType


class Data(BaseModel):

    def __init__(self, _id: int, _href: str, _type: DataType):
        self._id = _id
        self._href = _href
        self._type = _type


class Album(Data):

    def __init__(self, _id: int, _href: str):
        super().__init__(_id, _href, DataType.ALBUM)


class Artist(Data):

    def __init__(self, _id: int, _href: str):
        super().__init__(_id, _href, DataType.ARTIST)
