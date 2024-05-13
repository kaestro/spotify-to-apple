# models/Equivalent.py
from pydantic import BaseModel


class Equivalent(BaseModel):
    _id: str
    _region: str

    def __init__(self, id: str, region: str):
        self._id = id
        self._region = region

    def getId(self):
        return self._id

    def getRegion(self):
        return self._region
