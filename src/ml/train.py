import numpy as np
from numba import jit 
from multiprocessing.pool import ThreadPool
from models import getRandomForest , getStochasticGradientDescent , getSupportVectorMachine , plot_cf


def train(midpoint, imbalance , orderbook_pressure , count , N  ):

    arr = np.zeros((count , 2))
    iterate_arr(imbalance , orderbook_pressure , count , arr , N)

    vector = np.zeros(count)
    get_vector(count , vector , midpoint , imbalance , N)

    print("Initializing Model")
    model_svm = getStochasticGradientDescent(arr, vector)

    return model_svm

def plot(model , midpoint, imbalance , orderbook_pressure , count , N):

    arr = np.zeros((count , 2))
    iterate_arr(imbalance , orderbook_pressure , count , arr , N)

    vector = np.zeros(count)
    get_vector(count , vector , midpoint , imbalance , N)

    plot_cf(model , arr , vector)




# @jit(nopython = True, parallel = True)
def iterate_arr(temp_imbalance, temp_orderbook_pressure, doc_count, arr , N):
    """
    Parses Data Quickly with Numba 
    """

    for i in range(doc_count):

        x = temp_imbalance[i]["imbalance"][N-1]
        y = temp_orderbook_pressure[i]["orderbook_pressure"][N-1]
        temp = np.array([x, y])
        arr[i] = temp

    return 0

# @jit(nopython = True, parallel = True)
def get_vector(doc_count, vector, midpoint, imbalance, N):
    """
    Parses Data Quickly with Numba
    """


    for i in range(doc_count - 1):

        if imbalance[i]["imbalance"][N-1] > 0.50 and midpoint[i + 1]["mid_point"] > midpoint[i]["mid_point"]:
            vector[i] = 1

        if imbalance[i]["imbalance"][N-1] < 0.50 and midpoint[i + 1]["mid_point"] < midpoint[i]["mid_point"]:
            vector[i] = 1 

    return 0