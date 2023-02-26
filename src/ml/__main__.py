import os
from dotenv import load_dotenv

load_dotenv()
mongo_client = os.getenv('MONGO_CLIENT')

from mongo import Mongo
from train import train , plot



if __name__ == "__main__":

    client = Mongo(mongo_client)

    midpoint = client.fetch_midpoint()[0:100]
    imbalance = client.fetch_imbalance()[0:100]
    orderbook_pressure = client.fetch_orderbook_pressure()[0:100]
    count1 = 100
    count = client.getCount()
    N = 5000


    model = train(midpoint , imbalance , orderbook_pressure , count1 , N)
    print("model created")


    test_midpoint = client.fetch_midpoint()[100:]
    test_imbalance = client.fetch_imbalance()[100:]
    test_orderbook_pressure = client.fetch_orderbook_pressure()[100:]
    count = client.getCount()
    count2 = count - 100

    print(test_midpoint)


    plot(model , test_midpoint , test_imbalance , test_orderbook_pressure , count2 , N)