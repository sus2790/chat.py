from chat.author import Author
from chat.guild import Guild

__all__ = [
    "Message",
]

class Message(object):
    def __init__(self, data: str) -> None:
        self._data = data

    @property
    def author(self) -> Author:
        return Author(self._data)

    @property
    def guild(self) -> Guild:
        return Guild(self._data)

    @property
    def content(self):
        return self._data["text"]

    @property
    def created_at(self):
        return self._data["createTime"]
