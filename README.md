# Chat.py

> (正在開發中，這是beta版本)
**一個簡單、方便的Google Chat Webhook函式庫**

## 🚀 安裝

Chat.py 透過下列指令進行安裝

```sh
python3 -m pip install git+https://github.com/sus2790/chat.py
```

怎麼樣？簡單吧！心動不如行動，現在就試試看吧！

## 🔧 使用

```py
import asyncio
from chat.webhook import Webhook

webhook = Webhook("我是Webhook網址")


async def foo():
    await webhook.send("傑哥不要啦！")


asyncio.run(foo())

```

你可以在[這裡](examples)查看更多範例 ❤️
