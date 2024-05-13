from enums.DataType import DataType
from models.Apple.Relationships import Relationships
from models.TrackBase import TrackBase
from models.Apple.Attributes import AppleAttributes
from models.Apple.Equivalent import Equivalent


class Track(TrackBase):

    _HOME_URL = "https://music.apple.com/"

    def __init__(
        self,
        id: int,
        attrs: AppleAttributes,
        equi: list[Equivalent],
        rel: Relationships,
        country: str = "us",
    ):
        self._BASE_URL = Track._HOME_URL + country + "/album/"
        super().__init__(str(id), self._BASE_URL + str(id), DataType.TRACK)
        self.set_apple_music_id(id)
        self._attributes = attrs
        self._equivalents = equi
        self._relationships = rel

    def _set_id(self):
        self._id = str(self._apple_music_id)

    def set_apple_music_id(self, apple_music_id: int):
        self._apple_music_id = apple_music_id
        self._set_id()

    def get_apple_music_id(self):
        return self._apple_music_id

    def get_attributes(self):
        return self._attributes

    def get_equivalents(self):
        return self._equivalents

    def get_relationships(self):
        return self._relationships
