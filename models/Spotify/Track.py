from models.Spotify.TrackAdditionalInfo import TrackAdditionalInfo
from models.Spotify.TrackBasicInfo import TrackBasicInfo
from models.TrackBase import TrackBase
from enums.DataType import DataType


class Track(TrackBase):
    _BASE_URL = "https://api.spotify.com/v1/tracks/"

    def __init__(
        self,
        id,
        basicInfo: TrackBasicInfo,
        additionalInfo: TrackAdditionalInfo,
    ):
        super().__init__(id, Track._BASE_URL + basicInfo._uri, DataType.TRACK)
        self._basicInfo = basicInfo
        self._additionalInfo = additionalInfo
