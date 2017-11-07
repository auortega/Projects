# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:14:48 2016

@author: auort
"""

from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc


"""
Write code to generate and display a series difference of ratio images from an input image
"""

directory = 'C:\\Users\\auort\\Desktop\\CV_E4\\'

def Ratio (identifier, loop, ratio):
    #Open image, convert to grayscale, and save as array
    im  = Image.open(directory + '1.jpg')
    ratiostring = str(ratio)
    for i in xrange(loop):
        #get resized image
        height = int(float(im.size[1]) * ratio)
        width = int(float(im.size[0]) * ratio)
        print("Height: %s" % str(height))
        print("Width: %s" % str(width))
        if width > 0:
            if height > 0:
                R = im.resize((width, height), Image.ANTIALIAS)
                savevalue = str(i+1)
                scipy.misc.imsave(directory + identifier + '\\DifferenceRatio_'+ ratiostring + '_' + savevalue +'.jpg', R)
                
                im = R
            else:
                loop = i
        else:
            loop = i
    for j in xrange(loop):
        #get resized image
        height2 = int(float(im.size[1]) * (2-ratio))
        width2 = int(float(im.size[0]) * (2-ratio))
        print("Height: %s" % str(height2))
        print("Width: %s" % str(width2))
        if width > 0:
            if height > 0:
                R = im.resize((width2, height2), Image.ANTIALIAS)
                savevalue2 = str(j+1)
                scipy.misc.imsave(directory + identifier + '\\DifferenceRatioback_'+ ratiostring + '_' + savevalue2 +'.jpg', R)
                
                im = R

Ratio('2', 10, .95)    
Ratio('2', 10, .80)
Ratio('2', 10, .65)