import logging
from pymongo import MongoClient

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()


class Mongo():

    """
        Connect to MongoDb
    """
    def __init__(self , mgClient) -> None:

        try:
            self.client = MongoClient(mgClient)
            logger.info("Connected to mongodb")
            self.db = self.client["obdb"]
            self.coll = self.db["orderbook"]
            self.connection = True

        except:
            logger.debug("Error in connecting to mongodb")
            self.connection = False


    """
        Inserts the data to mongodb in specified format
    """
    def appendMongo(self , obj): 

        dict = {
            "timestamp": (obj.timestamp),

            "top_bid": str(obj.top_bid),
            "top_ask": str(obj.top_ask),
            "mid_point": str(obj.mid_point),

            "tot_bidSize": str(obj.tot_bidSize),
            "tot_askSize": str(obj.tot_askSize),

            "imbalance": str(obj.imbalance),
            "orderbook_pressure": str(obj.pressure),
            "weighted_midpoint": str(obj.weighted_midpoint)
        }
        resp = self.coll.insert_one(dict)
        logger.info("Response added" , resp)
        return 0


    """
        Fetches data from mongodb
    """
    def fetchMongo(self , stamp):

        resp =  self.coll.find({"timestamp": {"$gt": stamp} })
        return resp

    

