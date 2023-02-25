import logging
from pymongo import MongoClient
import json

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()


class Mongo():

    """
        Connect to MongoDb
    """
    def __init__(self , mgClient , clear_data) -> None:

        try:
            self.client = MongoClient(mgClient)
            print("Connected to mongodb")
            self.db = self.client["obdb"]
            self.coll = self.db["orderbook"]
            self.connection = True

            if clear_data:
                print("Clearing Previous Data")
                self.coll.delete_many({})

        except:
            print("Error in connecting to mongodb")
            self.connection = False


    """
        Inserts the data to mongodb in specified format
    """
    def appendMongo(self , obj): 

        dict = {
            "timestamp": (obj["timestamp"]),

            "top_bid": str(obj["top_bid"]),
            "top_ask": str(obj["top_ask"]),
            "mid_point": str(obj["mid_point"]),

            "tot_bidSize": str(obj["tot_bidSize"]),
            "tot_askSize": str(obj["tot_askSize"]),

            "imbalance": (obj["imbalance"]).tolist(),
            "orderbook_pressure": (obj["orderbook_pressure"]).tolist(),
            "weighted_midpoint": (obj["weighted_midpoint"]).tolist()
        }
        resp = self.coll.insert_one(dict)
        return 0


    """
        Fetches data from mongodb
    """
    def fetchMongo(self , stamp):

        resp =  self.coll.find({"timestamp": {"$gt": stamp} })
        return resp

