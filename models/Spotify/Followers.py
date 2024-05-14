# models/Spotify/Followers.py


class Followers:
    def __init__(self, total: int, href: str = None):
        self._href = href
        self._total = total

    def getHref(self):
        return self._href

    def getTotal(self):
        return self._total


def response_json_to_followers(response_json: dict):
    return Followers(
        response_json["total"],
        response_json["href"],
    )
