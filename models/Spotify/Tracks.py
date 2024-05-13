# models/Spotify/Tracks.py
from models.Spotify.Track import Track


class Tracks:
    def __init__(
        self,
        href: str,
        limit: int,
        offset: int,
        total: int,
        items: list[Track],
        next: str = None,
        previous: str = None,
    ):
        self._href = href
        self._limit = limit
        self._next = next
        self._offset = offset
        self._previous = previous
        self._total = total
        self._items = items

    @property
    def href(self):
        return self._href

    @property
    def limit(self):
        return self._limit

    @property
    def next(self):
        return self._next

    @property
    def offset(self):
        return self._offset

    @property
    def previous(self):
        return self._previous

    @property
    def total(self):
        return self._total

    @property
    def items(self):
        return self._items
