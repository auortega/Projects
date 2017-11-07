# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:52:15 2016

@author: auort
"""

from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import scipy.misc

directory = 'C:\\Users\\auort\\Desktop\\CV_E4\\'

def HOGGen(image, ax, ay, bx, by, barnumber):
    regionheight = by-ay
    regionwidth = bx-ax
    
    subregionheight = regionheight/2
    subregionwidth = regionwidth/2
    
    region = image[ay:by,:][:,ax:bx]
    
    #The region will be separated into four quadrant subregions and an overlapping center subregion
    subregionA = image[ay:ay+subregionheight,:][:,ax:ax+subregionwidth]#ax-> ax+subregionwidth
    subregionB = image[by-subregionheight:by,:][:,ax:ax+subregionwidth]
    subregionC = image[ay:ay+subregionheight,:][:,bx-subregionwidth:bx]
    subregionD = image[by-subregionheight:by,:][:,bx-subregionwidth:bx]
    
    scipy.misc.imsave(directory + '\\3\\Region.jpg', region)
    scipy.misc.imsave(directory + '\\3\\SubregionA.jpg', subregionA)   
    scipy.misc.imsave(directory + '\\3\\SubregionB.jpg', subregionB) 
    scipy.misc.imsave(directory + '\\3\\SubregionC.jpg', subregionC) 
    scipy.misc.imsave(directory + '\\3\\SubregionD.jpg', subregionD) 
    
    magnitudeA = subregionA
    getMagnitude(subregionA, magnitudeA)
    #hist(magnitudeA.flatten(), barnumber)
    #show()
    #histogram, binedges = histogram(magnitudeA.flatten(), barnumber, Density = true)
    #print(histogram)
    #scipy.misc.imsave(directory + '\\3\\HistogramA.jpg', hist)
    
    getGradient(region)
    #getGradient(subregionA)
    #getGradient(subregionB)
    #getGradient(subregionC)
    #getGradient(subregionD)
    
    
def getMagnitude(im, magnitude):
    
    #Sobel derivative filters 
    imx = zeros(im.shape) 
    filters.sobel(im,1,imx)
    
    imy = zeros(im.shape) 
    filters.sobel(im,0,imy)
    
    magnitude = sqrt(imx**2+imy**2)
    scipy.misc.imsave(directory + '\\3\\Magnitude.jpg', magnitude)

def getGradient (im):
    
    print "image = ", im
    
    gx, gy = gradient(im)
    print "gx = ", gx
    print "gy = ", gy
    print "gx: lenght: ",len(gx[0]) ,"width: ", len (gx)
    print "gy: lenght: ",len(gy[0]) ,"width: ", len (gy)
    
    scipy.misc.imsave(directory + '\\3\\Gx.jpg', gx)
    scipy.misc.imsave(directory + '\\3\\Gy.jpg', gy)
    rad = arctan2(gy, gx)
    print "radians: ", rad
    variableA = 180/math.pi
    deg = (rad*(variableA))
    print "degrees: ", deg
    
    hist(deg.flatten(), barnumber)
    show()
    
    
    
    

im = array(Image.open(directory + '1.jpg'))#Color image
im2 = array(Image.open(directory + '1.jpg').convert('L'))#Greyscale image

cornerAx = 500
cornerAy = 500
cornerBx = 700
cornerBy = 700
barnumber = 10 
magnitude = im2

HOGGen(im2,cornerAx, cornerAy, cornerBx, cornerBy, barnumber)

getMagnitude(im2, magnitude)