# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:06:43 2016

@author: auort
"""
from PIL import Image
from collections import *
from loadCIFAR2 import load_cifar
import plot
from HOG import imHOG
import numpy as np
import cv2


images, trainLabels = load_cifar("blackWhite","data_batch_1", "C:/Users/auort/Desktop/CV_L4/RCode/cifar-10-batches-py/")
div,bins = 4,4
histData = np.zeros((len(trainLabels),div*div,bins))
for i in range(len(images)):
    histData[i]= imHOG(images[i], div, bins)

histData = np.float32(histData)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

k = 10
compactness,labels,centers = cv2.kmeans(histData,k,None,criteria,10,flags)
labels = labels.flatten()

data = plot.getAccuracy(labels,k,trainLabels)
title = "Accuracy of Color Histograms as Features for Clustering"
xlabel = "Number of  Clusters"
ylabel = "Accuracy Percentage"
plot.plotData(data,[[-1,0],[k+1,100]], title, xlabel, ylabel)