# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:07:54 2016

@author: auort

Use k means clustering to posterize an image with n number of colors

"""

import numpy as np
import cv2
import scipy
from PIL import Image
import scipy.misc
import time
from pylab import *
import copy

def getarray(img):
    array = img.reshape((-1,3))
    array = np.float32(array) #cv2.kmeans needs float array, soarray must be converted
    return array

def getimage(array, label, img):
    array = np.uint8(array)#convert from float to int
    print ""
    print "array:"#this is what I need to match the colors
    print array
    imshow(array)
    
    
    print ""
    print "array[0]: %s"%array[0]
    
    return array
    
    '''
    colorspectrum = np.zeros((24,24,3))
    for i in range(24):
        colorspectrum[i]=array
    print ""
    print "colorspectrum:"
    print colorspectrum
    scipy.misc.imsave('colorspectrum.jpg', colorspectrum)
    '''
    
    '''
    result = array[label.flatten()]
    print ""
    print "result:"
    print result
    resultimage = result.reshape((img.shape))#convert to original shape
    return resultimage
    '''
    
def expandImage(Im):
    length = len(Im)*10
    height = len(Im[0])*10
    retIm = np.zeros((length, height, 3))
    for y in range(height):
        for x in range(length):
            indexx = int(x/10)
            indexy = int(y/10)
            retIm[x][y] = Im[indexx][indexy]
    return retIm

def posterize(imagename, numcolors, savedirectory):
    img = cv2.imread(imagename)
    #img2 = cv2.imread("//utep//passport.jpg")
    array = getarray(img)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)#stop iteration if epsilon is reached or if max iterations has occured; max iterations = 10, epsilon = 1.0
    ret,label,result=cv2.kmeans(array, numcolors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    print "label:"
    print label
    print ""
    print "ret:"
    print ret
    resultimage1 = getimage(result, label, img)
    return resultimage1
    #resultimage2 = getimage(result, label, img2)
    #cv2.imwrite(savedirectory, resultimage)

    '''
    cv2.imshow('posterized image using k means with k=' + str(numcolors) +' of '+ imagename, resultimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    
def getNeighbors(colors, passport):
    
    neighbors = copy.deepcopy(colors)
    for i in range (len(colors)):
        passportw = copy.deepcopy(passport)
        difference = copy.deepcopy(colors)
        passportw = abs(passportw-difference[i])
        print "passportw:"
        print passportw
        for j in range(len(colors)):
            difference[j]=passportw[j][0]+passportw[j][1]+passportw[j][2]
        neighbors[i] = np.argmin(difference)
    return neighbors
        

    
#posterize('harrysmall.jpg', 1, "harry1.jpg")
#posterize('harrysmall.jpg', 2, 'harry2.jpg')
#posterize('ImageCreated.jpg', 5, 'ImageCreated5.jpg')
print "Posterizing passport "
passport = posterize('passportlarge.jpg',24,'passport24.jpg')
print "Posterizing passport again"
colors = posterize('passportlarge.jpg',10,'passport10.jpg')
print "Posterizing colors"
#colors = posterize('uteppassport2.jpg',10,'passport24a.jpg')
print "Getting neighbors"
neighbors = getNeighbors(colors, passport)
print ""
print "Neighbors (15):"
print neighbors
#posterize('harrysmall.jpg', 10, 'harry10.jpg')
#posterize('harrysmall.jpg', 25, 'harry25.jpg')
