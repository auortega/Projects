# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:54:50 2016

@author: auort
"""

from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc

"""
Take an image and apply Gaussian blur like in Figure 1.9.
Plot the image contours for increasing values of theta. What
happens? Can you explain why?
"""

directory = 'C:\\Users\\auort\\Desktop\\CV_L1\\'

def construct (identifier, theta, degree):
    im  = array(Image.open(directory + identifier +'_Grayscale.jpg'))
    G = filters.gaussian_filter(im,theta)
    figure()
    gray()
    contour(G, origin='image')
    axis('equal')
    axis('off')
    figure()
    hist(G.flatten(),128)
    show()

    
construct('1',5,'5')
construct('1',10,'10')
construct('1',15,'15')
"""
construct('2',5,'5')
construct('2',10,'10')
construct('2',15,'15')
construct('3',5,'5')
construct('3',10,'10')
construct('3',15,'15')
construct('4',5,'5')
construct('4',10,'10')
construct('4',15,'15')
construct('5',5,'5')
construct('5',10,'10')
construct('5',15,'15')
"""
