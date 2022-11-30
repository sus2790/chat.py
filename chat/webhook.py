from typing import Optional

import aiohttp

from .exception import SendException

__all__ = [
    "Webhook",
]


class Webhook:
    """
    A class representing a Google Chat webhook.

    :param url: The URL of the webhook.
    :type url: str

    :ivar url: The URL of the webhook.
    """

    def __init__(self, url: str = None) -> None:
        self.url = url

    async def send(self, content: str, thread_id: Optional[str] = None) -> None:
        """
        Send a message to the webhook.

        :param content: The content of the message.
        :type content: str
        :param thread_id?: The thread ID of the message (if any).
        :type thread_id?: str
        """
        url = self.url + "&threadKey=" + thread_id if thread_id else self.url
        json = {"text": content}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json) as resp:
                data = await resp.json()
                if "error" in data:
                    raise SendException(data["error"]["message"])
                return Message(data)
