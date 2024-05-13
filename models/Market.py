# models/Market.py
from pydantic import BaseModel


class Market(BaseModel):

    def __init__(self, countryCode: str, name: str, currency: str):
        self._countryCode = countryCode
        self._marketName = name
        self._currency = currency

    def __str__(self):
        return self._countryCode

    def getCurrency(self):
        return self._currency

    def getCountryCode(self):
        return self._countryCode

    def getMarketName(self):
        return self._marketName
