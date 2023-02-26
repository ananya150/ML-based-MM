from pymongo import MongoClient
import json



class Mongo():

    """
        Connect to MongoDb
    """
    def __init__(self , mgClient) -> None:

        try:
            self.client = MongoClient(mgClient)
            print("Connected to mongodb")
            self.db = self.client["obdb"]
            self.coll = self.db["orderbook"]
            self.connection = True


        except:
            print("Error in connecting to mongodb")
            self.connection = False



    """
        Fetches data from mongodb with timestamp > stamp
    """
    def fetchMongo(self , stamp):

        resp =  self.coll.find({"timestamp": {"$gt": stamp} })
        return resp

    def fetch_midpoint(self):

        midpoint =  list(self.coll.find({}, {"mid_point":1, "_id":0}))
        return midpoint
    
    def fetch_imbalance(self):

        imbalance  = list(self.coll.find({}, {"imbalance":1, "_id":0}))
        return imbalance
    
    
    def fetch_orderbook_pressure(self):

        orderbook_pressure = list(self.coll.find({}, {"orderbook_pressure":1, "_id":0}))
        return orderbook_pressure
    
    def getCount(self):
        count = self.coll.count_documents({})
        return count

