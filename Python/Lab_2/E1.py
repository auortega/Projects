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
    
    #printGlobals()
    saveSelection()
    img = Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\13.jpg')
    image = np.array(img)
    selection = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\Selection.jpg'))
    
    """
    imagescaled1 = getscaledimage(img, 1.2)
    imagescaled2 = getscaledimage(img, 1.4)
    imagescaled3 = getscaledimage(img, 1.6)
    imagescaled4 = getscaledimage(img, 1.8)
    imagescaled5 = getscaledimage(img, 2.0)
    """
    image2 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\14.jpg'))
    image3 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\15.jpg'))
    image4 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\16.jpg'))
    image5 = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\17.jpg'))
    
    start_time = time.time()
    
    
    xval, yval = runPixelDetection(image, selection)
    drawareaofinterest(image, xval, yval, selection)
    xval, yval = runPixelDetection(image2, selection)
    drawareaofinterest(image2, xval, yval, selection)
    xval, yval = runPixelDetection(image3, selection)
    drawareaofinterest(image3, xval, yval, selection)
    xval, yval = runPixelDetection(image4, selection)
    drawareaofinterest(image4, xval, yval, selection)
    xval, yval = runPixelDetection(image5, selection)
    drawareaofinterest(image5, xval, yval, selection)
    
    """
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
    xval, yval = runPixelDetection(imagescaled5, selection)
    drawareaofinterest(imagescaled5, xval, yval, selection)
    """
    end_time = time.time()
    '''
    drawareaofinterest(image, xval, yval, selection)
    drawareaofinterest(imagescaled1, xval, yval, selection)
    drawareaofinterest(imagescaled2, xval, yval, selection)
    drawareaofinterest(imagescaled3, xval, yval, selection)
    '''
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

def drawareaofinterest(image, xval, yval, selection):
    x = xval*5
    y = yval*5
    #im = np.array(Image.open('stinkbug.png'), dtype=np.uint8)

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
    #print "saveSelection called!"
    global image
    selection = image[aY:bY,:][:,aX:bX]
    scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\Selection.jpg', selection)
    
def runPixelDetection(image, selection):
    #print "runPixelDetection called!"
    heightindex = 0
    widthindex = 0

    result = initializezeroarray((len(image)),(len(image[1])))
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
    while (heightindex < heightlimit):#height traversal
        widthindex = 0
        while (widthindex < widthlimit):#width traversal
            
            compare = (image[widthindex:(widthindex+len(selection)),:][:,heightindex:(heightindex+len(selection[0]))])
            if (len(compare)!= len(selection)):
                compare = deepcopy(selection)
                compare[compare > 0] = 0
            if (len(compare[0])!= len(selection[0])):
                compare = deepcopy(selection)
                compare[compare > 0] = 0

            #compare2 = selection[0:len(compare),:][:,0:len(compare[0])]
            
            subtraction = (compare) -(selection)

            subtraction[subtraction < 0] = 0

            avgsum = cumsum(cumsum(subtraction, 1), 0)#/(len(selection)*len(selection[1]))
            avgsum = avgsum.max(axis = 1)
            avgsum = avgsum.max(axis = 0)
            avgsum = avgsum.max()/(len(selection)*len(selection[1]))

            result[heightindex][widthindex] = avgsum
            
            resultmatrixheightindex = int(heightindex/5)
            resultmatrixwidthindex = int(widthindex/5)

            if(resultmatrixheightindex < len(resultmatrix)):
                #print "inside check for result matrix, resultmatrixheightindex < resultmatrix"   
                if (resultmatrixwidthindex < len(resultmatrix[0])):
                    #print "inside check for result matrix, resultmatrixheightindex < resultmatrix[0]"                
                    resultmatrix[resultmatrixheightindex][resultmatrixwidthindex] = avgsum
                    #print "        minval: %s" %minval
                    #print "        avgsum: %s" %avgsum
                    if (minval >= avgsum):
                        #print "                  minval checking to update minval indexes"
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
    #print "initializezeroarray called!"
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
directory = 'C:\\Users\\auort\\Desktop\\CV_L2\\'
im = Image.open(directory + '13.jpg')
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
