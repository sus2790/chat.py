import aiohttp
from typing import Optional, Union, List


class Webhook:
    def __init__(self, url: str = None) -> None:  
        self.url = url

    async def send(self, content: str):
       #TODO: Finish fetch.py
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json={"text": content}):
                return
