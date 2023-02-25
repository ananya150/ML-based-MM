import numpy as np


def getWeightedMidpoint(bids , asks, N):

    imbalance = np.zeros(N)
    w_midpoints = np.zeros(N)

    bid_kappa = 0
    ask_kappa = 0

    for i in range(N):

        bid_kappa += float(bids[i][0]) * float(bids[i][1]) 
        ask_kappa += float(asks[i][0]) * float(asks[i][1])
        imbalance[i] = bid_kappa / (bid_kappa + ask_kappa)
        w_midpoints[i] = (imbalance[i] * float(asks[i][0])) + ((1 - imbalance[i]) * float(bids[i][0]))

    return imbalance, w_midpoints



def getOrderBookPressure(bids, asks , N):
    """
    Input:
    1. The Currency Pair
    Computes the OrderBook Pressure Given the Current OrderBook
    PsuedoCode:
    1. If Best Ask Size > Best Bid Size --> Midpoint Decreases
    2. If Best Ask Size < Best Bid Size --> Midpoint Increases
    3. If Best Ask Size == Best Bid Size --> Midpoint Unchanged 
    Output:
    1. If Signal > 0 --> Bullish
    2. If Signal < 0 --> Bearish
    """

    pressure = np.zeros(N)

    bid_sum_size = 0
    ask_sum_size = 0

    for i in range(N):

        bid_sum_size += float(bids[i][1])
        ask_sum_size += float(asks[i][1])
        pressure[i] = bid_sum_size / ask_sum_size

    return pressure