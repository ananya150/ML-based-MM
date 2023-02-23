import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('API_KEY')
secret = os.getenv('API_SECRET')


import asyncio
import websockets
import json

msg = \
{
  "id" : 9344,
  "method" : "SUBSCRIBE",
  "params" : ["uniusdt@depth"]
}


url = "wss://stream.binance.com:9443/ws"


async def call_api(msg):
   async with websockets.connect(url) as websocket:
       print("0")
       await websocket.send(msg)
       print("1")
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           try:
              print(json.loads(response))
           except:
            pass


asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))

