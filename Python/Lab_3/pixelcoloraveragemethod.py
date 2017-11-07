# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:51:15 2016

@author: auort

Write a function to perform real-valued indexing on an image. Your function 
should receive an image I and the (real-valued) pixel coordinates < r, c > and 
return the RGB values of obtained by performing a weighted average of the 
pixels, where the weights are proportional to the area of overlap of the 
pixels in the original image and a hypothetical pixel centered at < r, c >. 
Use this function and regular rounding to evaluate the results of each of 
the methods from the following questions. 

"""

from PIL import Image
import scipy.misc
import cv2
import numpy as np
import time

def pixelcoloraverage(primes, image):
    #print "Primes: %s" % primes
    #image is an array with 3 channels
    cprime = primes[1]
    rprime = primes[0]
    c = int (cprime)#python always downcasts
    r = int (rprime)
    
    #distances
    dc2 = cprime - c
    dc1 = 1 - dc2
    dr2 = rprime - r
    dr1 = 1 - dr2

    vector1 = np.array([[dr1],[dr2]])
    vector2 = np.array([dc1,dc2])

    mask = vector1*vector2
    
    #print "Mask:"
    #print mask
    
    region = (image[c:c+2,:][:,r:r+2])
    
    sumred = 0
    sumgreen = 0
    sumblue = 0
    
    try:
        sumred = sumred + region[0][0][0] * mask[0][0]
        sumred = sumred + region[0][1][0] * mask[0][1]
        sumred = sumred + region[1][0][0] * mask[1][0]
        sumred = sumred + region[1][1][0] * mask[1][1]
        #print 'Sumred:%s' %sumred
        sumgreen = sumgreen + region[0][0][1] * mask[0][0]
        sumgreen = sumgreen + region[0][1][1] * mask[0][1]
        sumgreen = sumgreen + region[1][0][1] * mask[1][0]
        sumgreen = sumgreen + region[1][1][1] * mask[1][1]
        #print 'Sumgreen:%s' %sumgreen
        sumblue = sumblue + region[0][0][2] * mask[0][0]
        sumblue = sumblue + region[0][1][2] * mask[0][1]
        sumblue = sumblue + region[1][0][2] * mask[1][0]
        sumblue = sumblue + region[1][1][2] * mask[1][1]
        #print 'Sumblue:%s' %sumblue

    except IndexError:
        #print "Cprime: %s" % cprime
        #print "Rprime: %s" % rprime
        '''        
        sumred = image[c][r][0]
        sumgreen = image[c][r][1]
        sumblue = image[c][r][2]
        '''    
    return [int(sumred), int(sumgreen), int(sumblue)]    

image = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\14.jpg'))
image = (image[0:4,:][:,0:4])
#scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_E6\\Selection.jpg', image)
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

scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L3\\ImageCreated.jpg', image)
print 'Image created:'
print image
print ''
start_time = time.time()
avg1 = pixelcoloraverage([1.25, 1.25], image)
end_time = time.time()
runtime = end_time - start_time
print 'Averages 1.25, 1.25:'
print avg1
print 'Runtime: %s' % runtime
print ' '

start_time = time.time()
avg1 = pixelcoloraverage([1.75, 1.75], image)
end_time = time.time()
runtime = end_time - start_time
print 'Averages 1.75, 1.75:'
print avg1
print 'Runtime: %s' % runtime
print ' '


start_time = time.time()
avg1 = pixelcoloraverage([1.50, 1.50], image)
end_time = time.time()
runtime = end_time - start_time
print 'Averages 1.50, 1.50:'
print avg1
print 'Runtime: %s' % runtime
print ' '

start_time = time.time()
avg1 = pixelcoloraverage([1.25, 1.75], image)
end_time = time.time()
runtime = end_time - start_time
print 'Averages 1.25, 1.75:'
print avg1
print 'Runtime: %s' % runtime
print ' '

start_time = time.time()
avg1 = pixelcoloraverage([2, 2], image)
end_time = time.time()
runtime = end_time - start_time
print 'Averages 2, 2:'
print avg1
print 'Runtime: %s' % runtime
print ' '
