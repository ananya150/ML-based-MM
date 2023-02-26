import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


def getSupportVectorMachine(X, y):
    """
    Fits Support Vector Machine
    """

    model = svm.SVC(kernel = 'rbf', random_state = 0, tol = 1e-5)
    model.fit(X, y)

    return model

def getStochasticGradientDescent(X, y):
    """
    Fits Stochastic Gradient Descent
    """

    model = SGDClassifier(loss="hinge", penalty="l2", max_iter=1000)
    model.fit(X, y)

    return model

def getRandomForest(X, y,):
    """
    Fits Random Forest 
    """

    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(X, y)

    return model 

def plot_cf(model , X_test , y_test):

    predictions = model.predict(X_test)
    print(predictions)
    # cm = metrics.confusion_matrix(y_test, predictions, labels=model.classes_)
    # disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    # disp.plot()
    # plt.show()
