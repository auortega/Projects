# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 13:16:43 2016

@author: auort
"""

from PIL import Image
from numpy import *
import scipy.misc

directory = 'C:\\Users\\auort\\Desktop\\CV_L1\\'

def histeq(im,nbr_bins=256): 
    """ Histogram equalization of a grayscale image. """

    # get image histogram 
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True) 
    cdf = imhist.cumsum() # cumulative distribution function 
    cdf = 255 * cdf / cdf[-1] # normalize
    
    # use linear interpolation of cdf to find new pixel values 
    im2 = interp(im.flatten(),bins[:-1],cdf)
    
    return im2.reshape(im.shape), cdf

def construct (identifier):
    im  = array(Image.open(directory + identifier +'.jpg').convert('L'))
    scipy.misc.imsave(directory + identifier + '_Grayscale.jpg', im)
    im2,cdf = histeq(im)
    scipy.misc.imsave(directory +'P2\\'+identifier + '\\HistogramEqualization.jpg', im2)
    
construct('1')
construct('2')
construct('3')
construct('4')
construct('5')

