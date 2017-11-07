# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:48:28 2016

@author: auort
"""

import numpy as np
from loadMNIST import load_mnist
from sklearn.neighbors import KNeighborsClassifier
#from collections import *
import matplotlib.pyplot as plt

def train():
    trainIm, trainLb = load_mnist('training', digits=[0,1,2,3,4,5,6,7,8,9])
    trainIm = np.float32(trainIm).reshape((len(trainIm), -1))
    trainLb = trainLb.flatten()
    return trainIm, trainLb

def test():
    testIm, testLb = load_mnist('testing', digits=[0,1,2,3,4,5,6,7,8,9])
    testIm = np.float32(testIm).reshape((len(testIm), -1))
    testLb = testLb.flatten()
    return testIm, testLb
    
def plotResult(training, testing, boundaries, gtitle, xlbl, ylbl):
    plt.plot(*zip(*training), marker='o', color='b', ls='')
    plt.plot(*zip(*testing), marker='o', color='r', ls='')
    plt.plot(*zip(*boundaries), marker='o', color='w')
    plt.title(gtitle)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.show()
    
def classify(k):
    trainImages, trainLabels = train()
    testImages, testLabels = test()
    classifier = KNeighborsClassifier(n_neighbors=k,p=2)
    classifier.fit(trainImages[:30000], trainLabels[:30000])
    
    training = [[k,classifier.score(trainImages, trainLabels)]]
    testing = [[k,classifier.score(testImages, testLabels)]]
    boundaries = [[k-2,100],[k+2,100]]
    title = "Accuracy of Classification"
    xlabel = "Number of Neighbors"
    ylabel = "Accuracy Percentage"
    plotResult(training, testing, boundaries, title, xlabel, ylabel)

classify(20)