import os
from dotenv import load_dotenv

load_dotenv()
mongo_client = os.getenv('MONGO_CLIENT')

from database.mongo import Mongo
from database.webs import get_orderbook
from database.features import getOrderBookPressure,getWeightedMidpoint
import time
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()


def format_data(bids , asks , N) -> dict:

    timestamp = int(time.time())

    top_bid = float(bids[0][0])
    top_ask = float(asks[0][0])
    mid_point = (top_bid + top_ask)/2

    tot_bid_size = 0
    tot_ask_size = 0

    for i in range(N):
        tot_bid_size += float(bids[i][1])
        tot_ask_size += float(asks[i][1])


    imbalance , weighted_midpoint = getWeightedMidpoint(bids , asks , N)
    orderbook_pressure = getOrderBookPressure(bids , asks , N)

    obj = {
        "timestamp": timestamp,

        "top_bid": top_bid,
        "top_ask": top_ask,
        "mid_point": mid_point,

        "tot_bidSize": tot_bid_size,
        "tot_askSize": tot_ask_size,

        "imbalance": imbalance,
        "orderbook_pressure": orderbook_pressure,
        "weighted_midpoint": weighted_midpoint
        
    }

    return obj


if __name__ == "__main__":

    database = Mongo(mongo_client , True)


    while True:
        start = time.time()
        obData = get_orderbook(5000)
        print("Data Fetched")
        obj = format_data(obData["bids"] , obData["asks"] , 5000)
        print("Data Formatted" )
        database.appendMongo(obj)
        end = time.time()
        print("Latency is, " , (end-start)*1000 , " ms")
        print("---------------------------------------------------")

        time.sleep(10)

