# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:32:33 2016

@author: auort
"""

#Region select

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets
import scipy.misc
import time
from numpy import random
from scipy.ndimage import filters
from pylab import *
from numpy import *
from copy import copy, deepcopy
import matplotlib.patches as patches
from pylab import *
import scipy.misc



def onselect(eclick, erelease):
    global start_time
    global aX
    global aY
    global bX
    global bY
    
    
    
    if eclick.ydata>erelease.ydata:
        eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
    if eclick.xdata>erelease.xdata:
        eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
    ax.set_ylim(erelease.ydata,eclick.ydata)
    ax.set_xlim(eclick.xdata,erelease.xdata)
    fig.canvas.draw()
    
    """
    print 'aX: ',eclick.xdata
    print 'aY: ',eclick.ydata
    print 'bX: ',erelease.xdata
    print 'bY: ',erelease.ydata
    """
    aX = int(eclick.xdata)
    aY = int(eclick.ydata)
    bX = int(erelease.xdata)
    bY = int(erelease.ydata)
    
    printGlobals()
    saveSelection()
    img = Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\18.jpg').convert('L')
    image = np.array(img)
    selection = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\Selection.jpg').convert('L'))
    
    imagescaled1 = getscaledimage(img, 1.2)
    imagescaled2 = getscaledimage(img, 1.4)
    imagescaled3 = getscaledimage(img, 1.6)
    imagescaled4 = getscaledimage(img, 1.8)    
    
    """
    image2 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\14.jpg').convert('L'))
    image3 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\15.jpg').convert('L'))
    image4 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\16.jpg').convert('L'))
    image5 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\17.jpg').convert('L'))
    """
    start_time = time.time()
    
    
    xval, yval = runPixelDetection(image, selection)
    drawareaofinterest(image, xval, yval, selection)
    xval, yval = runPixelDetection(imagescaled1, selection)
    drawareaofinterest(imagescaled1, xval, yval, selection)
    xval, yval = runPixelDetection(imagescaled2, selection)
    drawareaofinterest(imagescaled2, xval, yval, selection)
    xval, yval = runPixelDetection(imagescaled3, selection)
    drawareaofinterest(imagescaled3, xval, yval, selection)
    xval, yval = runPixelDetection(imagescaled4, selection)
    drawareaofinterest(imagescaled4, xval, yval, selection)
    
    '''
    xval, yval = runHOGDetection(image, selection)
    drawareaofinterest(image, xval, yval, selection)
    '''
    '''
    xval, yval = runHOGDetection(image2, selection)
    drawareaofinterest(image2, xval, yval, selection)
    xval, yval = runHOGDetection(image3, selection)
    drawareaofinterest(image3, xval, yval, selection)
    xval, yval = runHOGDetection(image4, selection)
    drawareaofinterest(image4, xval, yval, selection)
    xval, yval = runHOGDetection(image5, selection)
    drawareaofinterest(image5, xval, yval, selection)
    '''
    
    
    end_time = time.time()
    drawareaofinterest(image, xval, yval, selection)
    print " "
    print "Time to finish: %s" %(end_time - start_time), " seconds"
    #scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\PixelbyPixel2.jpg', result)

def getscaledimage (img, scale):
    basewidth = int(img.size[0] * scale)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    imagescaled = np.array(img)
    return imagescaled

def HOGGen(image, ax, ay, bx, by, barnumber):
    regionheight = by-ay
    regionwidth = bx-ax
    
    subregionheight = int(regionheight/2)
    subregionwidth = int(regionwidth/2)
    
    #The region will be separated into four quadrant subregions and an overlapping center subregion
    subregionA = image[ay:ay+subregionheight,:][:,ax:ax+subregionwidth]#ax-> ax+subregionwidth
    subregionB = image[by-subregionheight:by,:][:,ax:ax+subregionwidth]
    subregionC = image[ay:ay+subregionheight,:][:,bx-subregionwidth:bx]
    subregionD = image[by-subregionheight:by,:][:,bx-subregionwidth:bx]
    
    histogram = getGradient(image)
    histogramA = getGradient(subregionA)
    histogramB = getGradient(subregionB)
    histogramC = getGradient(subregionC)
    histogramD = getGradient(subregionD)
    
    return histogram, histogramA, histogramB, histogramC, histogramD
    
    


def getGradient (im):
     
    gx, gy = gradient(im)
    rad = arctan2(gy, gx)
    variableA = 180/math.pi
    deg = (rad*(variableA))
    print deg.flatten()
    return deg.flatten()

def drawareaofinterest(image, xval, yval, selection):
    x = xval*5
    y = yval*5
    
    # Create figure and axes
    fig,ax = plt.subplots(1)
    
    # Display the image
    ax.imshow(image)
    
    # Create a Rectangle patch
    rect = patches.Rectangle((y,x),len(selection[0]),len(selection),linewidth=1,edgecolor='r',facecolor='none')
    
    # Add the patch to the Axes
    ax.add_patch(rect)
    
    plt.show()

def printGlobals():
    print 'aX: ',aX
    print 'aY: ',aY
    print 'bX: ',bX
    print 'bY: ',bY

def saveSelection():
    print "saveSelection called!"
    global image
    selection = image[aY:bY,:][:,aX:bX]
    scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\Selection.jpg', selection)
    
def runHOGDetection(image, selection):
    print "runPixelDetection called!"
    heightindex = 0
    widthindex = 0

    imageheight = len(image[1])
    heightlimit = (len(image)-len(selection))
    widthlimit = (len(image[0])-len(selection[0]))
    imagewidth = len(image)
    imageheight = len(image[0])
    selectheight = len(selection)
    selectwidth = len(selection[0])

    resultmatrixwidth = int(imagewidth/5)
    resultmatrixheight = int(imageheight/5)

    resultmatrix = initializezeroarray (resultmatrixwidth, resultmatrixheight)
    minval = 160;
    minvalx = 0;
    minvaly = 0;
    
    HO, HA, HB, HC, HD = HOGGen(selection, 0, 0, len(selection)-1, len(selection[0])-1, 10)
    
    while (heightindex < heightlimit):#height traversal
        widthindex = 0
        while (widthindex < widthlimit):#width traversal
            print "widthindex: %s." % widthindex
            print "widthlimit: %s." % widthlimit
            print "heightindex: %s." % heightindex
            print "heightlimit: %s." % heightlimit

            bx = selectwidth + widthindex
            by = selectheight + heightindex
            HO2, HA2, HB2, HC2, HD2 = HOGGen(image, widthindex, heightindex, bx, by, 10)

            if(len(HA2) != len(HA)):
                HA2 = deepcopy(HA)
                HA2[HA2 > 0] = 0
            if(len(HB2) != len(HB)):
                HB2 = deepcopy(HB)
                HB2[HB2 > 0] = 0
            if(len(HC2) != len(HC)):
                HC2 = deepcopy(HC)
                HC2[HC2 > 0] = 0
            if(len(HD2) != len(HD)):
                HD2 = deepcopy(HD)
                HD2[HD2 > 0] = 0
            
            #subO = (HO) - (HO2)
            subA = (HA) - (HA2)
            subB = (HB) - (HB2)
            subC = (HC) - (HC2)
            subD = (HD) - (HD2)
            
            #making sure subs only have positive values
            #subO[subO < 0] = 0
            subA[subA < 0] = 0
            subB[subB < 0] = 0
            subC[subC < 0] = 0
            subD[subD < 0] = 0
            
            
            avgsumA = cumsum(subA, 0)#/(len(selection)*len(selection[1]))
            avgsumA = avgsumA.max(axis = 0)
            avgsumA = avgsumA.max()/len(subA)
            
            avgsumB = cumsum(subB, 0)#/(len(selection)*len(selection[1]))
            avgsumB = avgsumB.max(axis = 0)
            avgsumB = avgsumB.max()/len(subB)
            
            avgsumC = cumsum(subC, 0)#/(len(selection)*len(selection[1]))
            avgsumC = avgsumC.max(axis = 0)
            avgsumC = avgsumC.max()/len(subC)
            
            avgsumD = cumsum(subD, 0)#/(len(selection)*len(selection[1]))
            avgsumD = avgsumD.max(axis = 0)
            avgsumD = avgsumD.max()/len(subD)
            
            avgsum = avgsumA + avgsumB + avgsumC + avgsumD / 4
            npixsubregions = len(selection/4)*len(selection[1]/4)            
            
            resultmatrixheightindex = int(heightindex/5)
            resultmatrixwidthindex = int(widthindex/5)

            if(resultmatrixheightindex < len(resultmatrix)):
                #print "inside check for result matrix, resultmatrixheightindex < resultmatrix"   
                if (resultmatrixwidthindex < len(resultmatrix[0])):
                    #print "inside check for result matrix, resultmatrixheightindex < resultmatrix[0]"                
                    resultmatrix[resultmatrixheightindex][resultmatrixwidthindex] = avgsum

                    if (minval >= avgsum):
                        minval = avgsum
                        minvalx = resultmatrixwidthindex
                        minvaly = resultmatrixheightindex

            widthindex = widthindex + 5
            
        heightindex = heightindex + 5
        if(widthindex >= len(image[0]) + 1):
            print "Caught out of bounds"
            break

    return minvalx, minvaly    
    
def initializezeroarray(w, h):
    print "initializezeroarray called!"
    zeroarray = [[0 for x in range(h)] for y in range(w)]
    return zeroarray
    
def getSelectionWidth():
    print "getSelectionWidth called!"
    return (bX-aX)
    
def getSelectionHeight():
    print "getSelectionHeight called!"
    return (bY-aY)

identifier = 1
stringidentifier = str(identifier)
fig = plt.figure()
ax = fig.add_subplot(111)
directory = 'C:\\Users\\auort\\Desktop\\CV_L3\\'
im = Image.open(directory + 'book.jpg')
image = np.array(im)
aX = 0
aY = 0
bX = 0
bY = 0
start_time = 0

arr = np.asarray(im)
plt_image=plt.imshow(arr)
rs=widgets.RectangleSelector(
    ax, onselect, drawtype='box',
    rectprops = dict(facecolor='red', edgecolor = 'black', alpha=0.5, fill=True))
plt.show()
