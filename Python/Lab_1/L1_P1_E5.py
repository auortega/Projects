# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 12:08:27 2016

@author: auort
"""
from PIL import Image
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc
import cv2

"""
Use gradient direction and magnitude to detect lines in an image. Estimate the
extent of the lines and their parameters. Plot the lines overlaid on the image.
"""


directory = 'C:\\Users\\auort\\Desktop\\CV_E3\\'



def construct (identifier, n, m):
    #Original image
    im = Image.open(directory+ identifier +'.jpg').convert('L')
    im1 = array(im)
    
    im2 = array(im.crop((n, n, len(im1[0]), len(im1))))
    
    im3 = array(im.crop((0, 0, len(im1[0])-n, len(im1)-n)))
    
    
    scipy.misc.imsave(directory + identifier + '\\Original_'+ m +'.jpg', im1)
    scipy.misc.imsave(directory + identifier + '\\Shifted_'+ m +'.jpg', im2)
    scipy.misc.imsave(directory + identifier + '\\Cropped_'+ m +'.jpg', im3)
    
    im4 = ((im2 - im3))
    
    scipy.misc.imsave(directory + identifier + '\\Result_'+ m +'.jpg', im4)
    (thresh, im5) = cv2.threshold(im4, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(directory + identifier + '\\Binary_'+ m +'.jpg', im5)
    
    im6 = im2 + im5
    
    scipy.misc.imsave(directory + identifier + '\\Final_'+ m +'.jpg', im6)
    
def run (n):
    construct(n, 1, '1')
    construct(n, 5, '5')
    construct(n, 10, '10')
    construct(n, 20, '20')

run('1')
"""
run('2')
run('3')
run('4')
run('5')
run('6')
"""
