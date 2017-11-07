# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:58:14 2016

@author: auort
"""

from PIL import Image
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc

"""
Implement an unsharp masking operation (http:en.wikipedia.org/wiki/Unsharp_
masking) by blurring an image and then subtracting the blurred version from the
original. this gives a sharpening effect to the image. Try this on both color 
and grayscale images.

"""

directory = 'C:\\Users\\auort\\Desktop\\CV_L1\\'

def construct (identifier, theta, degree, amount, tag):
    #Original images
    im1  = array(Image.open(directory + identifier +'.jpg'))
    im2  = array(Image.open(directory + identifier +'_Grayscale.jpg'))
    
    #Blurred images
    G1 = filters.gaussian_filter(im1,theta)
    G2 = filters.gaussian_filter(im2,theta)
    """
    #Blurred and inverted images
    C1 = 255 - B1
    C2 = 255 - B2
    #Blurred, inverted, and clamped images
    D1 = (1.0/255) * C1 + 100
    D2 = (1.0/255) * C1 + 100
    #Blurred, inverted, and clamped + Original
    E1 = D1 + A1
    E2 = D2 + A2
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpened_Color_' + degree + '.jpg', E1)
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpened_Grayscale_' + degree + '.jpg', E2)
    """
    
    M1 = (im1-G1)
    M2 = (im2-G2)
    S1 = im1 + M1 * amount
    S2 = im2 + M2 * amount
    I1 = 255 - M1
    I2 = 255 - M2
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Color_' + degree + '_' + tag +'.jpg', S1)
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Grayscale_' + degree + '_' + tag + '.jpg', S2)
    """
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpening_Color_' + degree + '.jpg', S1)
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpening_Grayscale_' + degree + '.jpg', S2)
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpening_Color_Invert_' + degree + '.jpg', S3)
    scipy.misc.imsave(directory + 'P1\\E2\\' + identifier + '\\Sharpening_Grayscale_Invert_' + degree + '.jpg', S4)
    """
    
def run (n):
    construct(n, 1, '1', .1, '.1')
    construct(n, 10, '10', .1, '.1')
    construct(n, 20, '20', .1, '.1')
    construct(n, 50, '50', .1, '.1')
    construct(n, 100, '100', .1, '.1')
    construct(n, 200, '200', .1, '.1')
    construct(n, 300, '300', .1, '.1')
    
    construct(n, 1, '1', .5, '.5')
    construct(n, 10, '10', .5, '.5')
    construct(n, 20, '20', .5, '.5')
    construct(n, 50, '50', .5, '.5')
    construct(n, 100, '100', .5, '.5')
    construct(n, 200, '200', .5, '.5')
    construct(n, 300, '300', .5, '.5')
    
    construct(n, 1, '1', .9, '.9')
    construct(n, 10, '10', .9, '.9')
    construct(n, 20, '20', .9, '.9')
    construct(n, 50, '50', .9, '.9')
    construct(n, 100, '100', .9, '.9')
    construct(n, 200, '200', .9, '.9')
    construct(n, 300, '300', .9, '.9')
        
    
run('1')
run('2')
run('3')
run('4')
run('5')