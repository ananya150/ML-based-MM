# Fetching orderbook data using http requests
import asyncio
import json
import requests


def get_orderbook(N):
    api_url = f'https://api.binance.com/api/v3/depth?symbol=ETHUSDT&limit={N}'
    response = requests.get(api_url)
    return response.json()

