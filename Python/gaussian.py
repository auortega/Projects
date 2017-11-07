# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:46:30 2016

@author: auort
"""

from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc


"""
Write code to generate and display a series difference of Gaussian images from an input image
"""

directory = 'C:\\Users\\auort\\Desktop\\CV_E4\\'

def Gauss (identifier, loop, theta):
    #Open image, convert to grayscale, and save as array
    im  = array(Image.open(directory + identifier + '.jpg').convert('L'))
    thetastring = str(theta)
    for i in xrange(loop):
        #Apply Gaussian filter to im, using theta 
        G = filters.gaussian_filter(im,theta)
        savevalue = str(i+1)
        result = im - G
        scipy.misc.imsave(directory + identifier + '\\DifferenceGaussian_'+ thetastring + '_' + savevalue +'.jpg', result)
        
        im = G
    

Gauss('1', 10, 2)    
Gauss('1', 10, 5)
Gauss('1', 10, 7)