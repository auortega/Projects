# -*- coding: utf-8 -*-
"""
Created on Tue Nov 8 09:44:32 2016

@author: auort
"""

from pylab import *
import numpy as np
import cv2
from loadMNIST import load_mnist
import matplotlib.pyplot as plt

def classify_digit(digit, labelled_centroids):
    print "classify_digit called!"

    mindistance = float("inf")
    for (label, centroid) in labelled_centroids:
        distance = np.linalg.norm(centroid - digit)
        if distance < mindistance:
            mindistance = distance
            closest_centroid_label = label
    return closest_centroid_label

def get_error_rate(digits,labelled_centroids):
    print "get_error_rate called!"

    classified_incorrect = 0
    for (label,digit) in digits:
        classified_label = classify_digit(digit, labelled_centroids)
        if classified_label != label:
            classified_incorrect +=1
    error_rate = classified_incorrect / float(len(digits))
    return error_rate

trainImages, trainLabels = load_mnist('training', digits=[0,1,2,3,4,5,6,7,8,9])
trainImages = np.float32(trainImages)
trainLabels = trainLabels.flatten()

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Set flags (Just to avoid line break in the code)
flags = cv2.KMEANS_RANDOM_CENTERS

error_rates = {x:None for x in range(10,,10)+[100]}

k = 10

# Apply KMeans
compactness,labels,centers = cv2.kmeans(trainImages,k,None,criteria,10,flags)

error_rate = get_error_rate(centers, labels)
error_rates[k] = error_rate

k = 20

# Apply KMeans
compactness,labels,centers = cv2.kmeans(trainImages,k,None,criteria,10,flags)

error_rate = get_error_rate(centers, labels)
error_rates[k] = error_rate

# Show the error rates
x_axis = sorted(error_rates.keys())
y_axis = [error_rates[key] for key in x_axis]
plt.figure()
plt.title("Error Rate by Number of Clusters")
plt.scatter(x_axis, y_axis)
plt.xlabel("Number of Clusters")
plt.ylabel("Error Rate")
plt.show()

'''
i = 0
for i in range(k):
    img1 = (centers[i,:])
    img1 = np.reshape(img1, (28,28))
    cv2.imwrite("centroidsB20_%d" % (i,) + ".png", img1)
    figure()
    gray()
    imshow(img1)
'''
