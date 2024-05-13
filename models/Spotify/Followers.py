# models/Spotify/Followers.py


class Followers:
    def __init__(self, total: int, href: str = None):
        self._href = href
        self._total = total

    def getHref(self):
        return self._href

    def getTotal(self):
        return self._total
