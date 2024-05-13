from models.SpotifyTrackAdditionalInfo import SpotifyTrackAdditionalInfo
from models.SpotifyTrackBasicInfo import SpotifyTrackBasicInfo
from models.Track import Track
from enums.DataType import DataType


class SpotifyTrack(Track):
    _BASE_URL = "https://api.spotify.com/v1/tracks/"

    def __init__(
        self,
        id,
        basicInfo: SpotifyTrackBasicInfo,
        additionalInfo: SpotifyTrackAdditionalInfo,
    ):
        super().__init__(id, SpotifyTrack._BASE_URL + basicInfo._uri, DataType.TRACK)
        self._basicInfo = basicInfo
        self._additionalInfo = additionalInfo
