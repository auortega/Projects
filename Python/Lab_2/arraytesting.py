# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:16:32 2016

@author: auort
"""

from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc

directory = 'C:\\Users\\auort\\Desktop\\CV_L2\\'

array = array([[0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0]])
array = array+50
scipy.misc.imsave(directory + '\\TestingArrays\\Array1.jpg', array)

array = insert(array,0,70,axis=1)
scipy.misc.imsave(directory + '\\TestingArrays\\Arrayaddcolumn0.jpg', array)

array = insert(array,0,50,axis=0)
scipy.misc.imsave(directory + '\\TestingArrays\\Arrayaddrow0.jpg', array)

array2 = array
print array2
array2 = array2 + 15
print array2
array3 = array2-array
print array3
scipy.misc.imsave(directory + '\\TestingArrays\\Array3.jpg', array3)
array4 = array-array2
array5 = array4.copy()
scipy.misc.imsave(directory + '\\TestingArrays\\Array4.jpg', array4)
print array4
array5[array5 < 0] = 0
print array5
