# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:51:15 2016

@author: auort
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets
import scipy.misc
import time
from numpy import random
from scipy.ndimage import filters
from pylab import *
from numpy import *
from copy import copy, deepcopy
import matplotlib.patches as patches



def pixelcoloraverage(cprime, rprime, image):
    #image is an array with 3 channels

    c = int (cprime)#python always downcasts
    r = int (rprime)
    
    #distances
    dc2 = cprime - c
    dc1 = 1 - dc2
    dr2 = rprime - r
    dr1 = 1 - dr2
    
    vector1 = array([[dr1],[dr2]])
    print vector1
    vector2 = array([dc1,dc2])
    
    mask = vector1*vector2
    
    #maskarray = array([[mask[0][0]],[mask[0][1]]],[[mask[1][0]],[mask[1][1]]])
    #print maskarray
    region = (image[c:c+2,:][:,r:r+2])
    print 'Region: '
    print region
    print 'Region[0]: ' 
    print region[0]
    print 'Mask:'
    print mask
    average1 = mask * region.take((0,), axis=2)
    print average1
    
    
    average1 = mask * region[z][0]
    average1 = cumsum(cumsum(average1,1),0)
    average1 = average1.max(axis = 1)
    average1 = average1.max(axis = 0)
    average2 = mask * region[1]
    average2 = cumsum(cumsum(average2,1),0)
    average2 = average2.max(axis = 1)
    average2 = average2.max(axis = 0)
    average3 = mask * region[2]
    average3 = cumsum(cumsum(average3,1),0)
    average3 = average3.max(axis = 1)
    average3 = average3.max(axis = 0)
    
    return average1, average2, average3    
    
image = array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\14.jpg'))
image = (image[0:4,:][:,0:4])
scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_E6\\Selection.jpg', image)
print len(image)
print len(image[0])
image[0][0] = [0,0,0]
image[0][1] = [20,0,20]
image[0][2] = [40,0,40]
image[0][3] = [60,0,60]

image[1][0] = [0,20,20]
image[1][1] = [20,20,40]
image[1][2] = [40,20,60]
image[1][3] = [60,20,40]    

image[2][0] = [0,40,40]
image[2][1] = [20,40,60]
image[2][2] = [40,40,40]
image[2][3] = [60,40,20]

image[3][0] = [0,60,60]
image[3][1] = [20,60,40]
image[3][2] = [40,60,20]
image[3][3] = [60,60,0]

scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_E6\\ImageCreated.jpg', image)

avg1, avg2, avg3 = pixelcoloraverage(1.25, 1.25, image)
print ' '
print 'Averages 1.25:'
print avg1
print avg2
print avg3

avg1, avg2, avg3 = pixelcoloraverage(1.75, 1.75, image)
print ' '
print 'Averages 1.75:'
print avg1
print avg2
print avg3

avg1, avg2, avg3 = pixelcoloraverage(1.50, 1.50, image)
print ' '
print 'Averages 1.50:'
print avg1
print avg2
print avg3