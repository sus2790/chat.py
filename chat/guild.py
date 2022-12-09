__all__ = [
    "Guild",
]

class Guild(object):
    def __init__(self, data: str) -> None:
        self._data = data

    @property
    def name(self):
        return self._data["space"]["displayName"]

    @property
    def type(self):
        return self._data["space"]["type"]

    @property
    def rule(self):
        return self._data["spaceDetails"]["guidelines"]

    @property
    def description(self):
        return self._data["spaceDetails"]["description"]
