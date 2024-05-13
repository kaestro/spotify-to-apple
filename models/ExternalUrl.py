# models/ExternalUrl.py
from pydantic import BaseModel


class ExternalUrl(BaseModel):

    def __init__(self, platformName: str, url: str):
        self._platformName = platformName
        self._url = url

    def getPlatformName(self):
        return self._platformName

    def getUrl(self):
        return self._url


class ExternalUrls(BaseModel):

    def __init__(self):
        self._external_urls: map[str, str]

    def addExternalUrl(self, externalUrl: ExternalUrl):
        self._external_urls[externalUrl.getPlatformName()] = externalUrl.getUrl()
