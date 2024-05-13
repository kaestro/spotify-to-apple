from enums.DataType import DataType
from models.Track import Track
from models.AppleRelationships import AppleRelationships
from models.Attributes import AppleAttributes
from models.Equivalent import Equivalent


class AppleMusicTrack(Track):

    _HOME_URL = "https://music.apple.com/"

    def __init__(
        self,
        id: int,
        attrs: AppleAttributes,
        equi: list[Equivalent],
        rel: AppleRelationships,
        country: str = "us",
    ):
        self._BASE_URL = AppleMusicTrack._HOME_URL + country + "/album/"
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
