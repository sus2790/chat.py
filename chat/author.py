__all__ = [
    "Author",
]


class Author(object):
    def __init__(self, data: str) -> None:
        self._data = data

    @property
    def name(self):
        return self._data["sender"]["displayName"]

    @property
    def type(self):
        return self._data["sender"]["type"]

    @property
    def avatar_url(self):
        return self._data["sender"]["avatarUrl"]

    @property
    def created_at(self):
        return self._data["createTime"]
