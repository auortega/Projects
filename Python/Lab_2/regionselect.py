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



def onselect(eclick, erelease):
    global start_time
    global aX
    global aY
    global bX
    global bY
    
    start_time = time.time()
    
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
    image = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\2.jpg'))
    selection = np.array(Image.open('C:\\Users\\auort\\Desktop\\CV_L2\\Selection.jpg'))
    result = runPixelDetection(image, selection)
    scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\PixelbyPixel2.jpg', result)

def printGlobals():
    print 'aX: ',aX
    print 'aY: ',aY
    print 'bX: ',bX
    print 'bY: ',bY

def saveSelection():
    print "saveSelection called!"
    global image
    selection = image[aY:bY,:][:,aX:bX]
    scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\\\Selection.jpg', selection)
    
def runPixelDetection(image, selection):
    print "runPixelDetection called!"
    heightindex = 0
    widthindex = 0
    print "image length: %s." % len(image)
    print "image height: %s." % len(image[1])
    result = initializezeroarray((len(image)),(len(image[1])))
    print "Result length: %s." % len(result)
    print "Result height: %s." % len(result[1])
    compareimageh = expandimagewithzeros(selection, result)
    print "compareimageh length: %s." % len(compareimageh)
    print "compareimageh height: %s." % len(compareimageh[1])
    compareimagev = deepcopy(compareimageh)
    while (heightindex < (len(image[0])-len(selection[0]))):#height traversal
        widthindex = 0
        while (widthindex < (len(image)-len(selection))):#width traversal
            #apply selection as a mask at point (heightindex, widthindex)
            print "Loop index: %s" %widthindex
            print ", %s" %heightindex
            compareimageh = deepcopy(compareimagev)
            result = result + (compareimageh - image)
            widthindex = widthindex + 5
            compareimageh = add5columns(compareimageh)
            #end nested while loop
        heightindex = heightindex + 5
        compareimagev = add5rows(compareimagev)
        #end while loop
    retval = result.copy()
    retval[retval < 0] = 0
    return retval
        
def initializezeroarray(w, h):
    print "initializezeroarray called!"
    zeroarray = [[0 for x in range(h)] for y in range(w)]
    return zeroarray
    
def expandimagewithzeros(selec, zeroimage):
    selection = deepcopy(selec)
    print "expandimagewithzeros called!"
    print "zeroimage length: %s." % len(zeroimage)
    print "zeroimage height: %s." % len(zeroimage[1])
    retarray = deepcopy(zeroimage)
    print "retarray length: %s." % len(retarray)
    print "retarray height: %s." % len(retarray[1])
    print "selection length: %s." % len(selection)
    print "selection height: %s." % len(selection[1])
    w = len(selection)
    h = len(selection[1])
    w = w-1
    h = h-1
    #for i in xrange(h-1):
    #    for j in xrange(w-1):
    #        retarray[j][i] = selection[j][i]
    #retarray = [[(selection[x][y]) for x in xrange(w)] for y in xrange(h)]
    
    for i in xrange(w,len(zeroimage)):
        for j in xrange(h,len(zeroimage[1])):
            selection = insert(selection,0,0,axis=0)
        selection = insert(selection,0,0,axis=1)
    output = selection
    #retarray[0:w+1, 0:h+1] = [[(selection[x][y]) for x in range(h)] for y in range(w)]
    print "retarray length: %s." % len(retarray)
    print "retarray height: %s." % len(retarray[1])
    #scipy.misc.imsave('C:\\Users\\auort\\Desktop\\CV_L2\\\\Selection2.jpg', retarray)
    #output = numpy.delete(retarray, [ : ], 2)
    return output
    
def getSelectionWidth():
    print "getSelectionWidth called!"
    return (bX-aX)
    
def getSelectionHeight():
    print "getSelectionHeight called!"
    return (bY-aY)

def add5rows(arr):
    print "add5rows called!"
    width = len(arr)
    height = len(arr[0])
    arr = insert(arr,0,0,axis=1)
    arr = insert(arr,0,0,axis=1)
    arr = insert(arr,0,0,axis=1)
    arr = insert(arr,0,0,axis=1)
    arr = insert(arr,0,0,axis=1)
    im = arr[0:width, 0:height]
    return im
    
def add5columns(arr):
    print "add5columns called!"
    array = arr.copy()
    array = insert(array,0,0,axis=0)
    array = insert(array,0,0,axis=0)
    array = insert(array,0,0,axis=0)
    array = insert(array,0,0,axis=0)
    array = insert(array,0,0,axis=0)
    im = array[0:len(arr), 0:len(arr[0])]
    return im
    

identifier = 1
stringidentifier = str(identifier)
fig = plt.figure()
ax = fig.add_subplot(111)
directory = 'C:\\Users\\auort\\Desktop\\CV_L2\\'
im = Image.open(directory + stringidentifier + '.jpg')
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



#plt.savefig(directory+stringidentifier+'_selection.jpg')
