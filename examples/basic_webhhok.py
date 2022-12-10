import asyncio
from chat.webhook import Webhook
#導入這個函式庫

webhook = Webhook("網址")
#設定webhook網址

async def foo():
    message = await webhook.send("傑哥不要啦！")
    #顯示發送的訊息
    print(message.content)

#開始運行webhook  
asyncio.run(foo())
