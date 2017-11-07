# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 12:01:49 2016

@author: auort
"""
from PIL import Image
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc

"""
An alternative image normalization to histogram equalization is a quotient 
image. A quotient image is obtained by diving the image with a blurred version
I/(I*G(sub-theta)). Implement this and try it on some sample images. 
"""

directory = 'C:\\Users\\auort\\Desktop\\CV_L1\\'

def construct (identifier, theta, degree):
    #Original images
    im1  = array(Image.open(directory + identifier +'.jpg'))
    im2  = array(Image.open(directory + identifier +'_Grayscale.jpg'))
    
    #Blurred images
    G1 = filters.gaussian_filter(im1,theta)
    G2 = filters.gaussian_filter(im2,theta)
    
    D1 = im1*G1
    D2 = im2*G2
    
    S1 = im1 / D1
    S2 = im2 / D2
    
    R1 = im1 - S1
    R2 = im2 - S2
    
    scipy.misc.imsave(directory + 'P1\\E3\\' + identifier + '\\Color_' + degree + '.jpg', R1)
    scipy.misc.imsave(directory + 'P1\\E3\\' + identifier + '\\Grayscale_' + degree + '.jpg', R2)
    
    
def run (n):
    construct(n, 1, '1')
    construct(n, 10, '10')
    construct(n, 20, '20')
    construct(n, 50, '50')
    construct(n, 100, '100')
    construct(n, 200, '200')
    construct(n, 300, '300')
        
"""
run('1')
"""
run('2')
run('3')
run('4')
run('5')
