# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:29:11 2016

@author: auort
"""

from loadCIFAR2 import load_cifar
import numpy as np
import cv2
import plot

def getCH(Im,n):
    colorHistogram = np.zeros((3,n))
    barSize = 255/(n-1)
    for i in range(len(Im)):
        for j in range(len(Im[i])):
            for k in range(3):
                index = Im[i][j][k]/barSize                    
                colorHistogram[k][index] = colorHistogram[k][index]+1
    return colorHistogram.flatten()

images, trainLabels = load_cifar("color","data_batch_1", "C:/Users/auort/Desktop/CV_L4/RCode/cifar-10-batches-py/")
bins = 16
dataCH = np.zeros((len(trainLabels),bins*3))
for i in trainLabels:
    dataCH[i]= getCH(images[i], bins)

dataCH = np.float32(dataCH)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

k = 20
compactness,labels,centers = cv2.kmeans(dataCH,k,None,criteria,10,flags)
labels = labels.flatten()

data = plot.getAccuracy(labels,k,trainLabels)
title = "Accuracy of Color Histograms as Features for Clustering"
xlabel = "Number of  Clusters"
ylabel = "Accuracy Percentage"
plot.plotData(data,[[-1,0],[k+1,100]], title, xlabel, ylabel)


