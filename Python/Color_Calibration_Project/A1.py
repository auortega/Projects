# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:06:58 2016

@author: auort
"""

import numpy as np
from PIL import Image
import scipy.misc
import time
from pylab import *
from numpy import *

def getSelection(Path):
    image = np.array(Image.open(Path))
    imshow(image)
    refPt = ginput(1)
    point = refPt[0]
    xcoor = int(point[0])
    ycoor = int(point[1])
    color = image[ycoor][xcoor]
    return color
    
def getPixel(Path,x,y):
    image = np.array(Image.open(Path))
    return image[x][y]

def runCallibration(Path1, Path2, Path3):
    showColor = getSelection(Path1)
    trueColor = getSelection(Path2)
    callibratedImage = callibrateImage(Path1, showColor, trueColor)
    scipy.misc.imsave(Path3, callibratedImage)
    
def callibrateImage(Path, showColor, trueColor):
    start_time = time.time()
    rT = trueColor[0]
    gT = trueColor[1]
    bT = trueColor[2]
    rS = showColor[0]
    gS = showColor[1]
    bS = showColor[2]

    colordifference = trueColor - showColor
    print "color difference:"
    print colordifference
    image = np.array(Image.open(Path))

    isRedSum = (trueColor[0]>showColor[0])
    isGreenSum = (trueColor[1]>showColor[1])
    isBlueSum = (trueColor[2]>showColor[2])
    print "isRedSum: %s" % isRedSum
    print "isGreenSum: %s" % isGreenSum
    print "isBlueSum: %s" % isBlueSum

    rabsdif = abs(rT-rS)
    gabsdif = abs(gT-gS)
    babsdif = abs(bT-bS)
    if (not(isRedSum)):
        rabsdif = 255-rabsdif
    if (not(isGreenSum)):
        gabsdif = 255-gabsdif
    if (not(isBlueSum)):
        babsdif = 255-babsdif
    print "red abs diff: %s" %rabsdif
    print "green abs diff: %s" %gabsdif
    print "blue abs diff: %s" %babsdif
    
    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
    
    redNthres = rabsdif
    greenNthres = gabsdif
    blueNthres = babsdif
    
    redPthres = 255-rabsdif
    greenPthres = 255-gabsdif
    bluePthres = 255-babsdif
    
    
    print "Negative Thresholds:"
    print "     redNthres: %s" %redNthres
    print "     greenNthres: %s" %greenNthres
    print "     blueNthres: %s" %blueNthres
    print "Positive Thresholds:"
    print "     redPthres: %s" %redPthres
    print "     greenPthres: %s" %greenPthres
    print "     bluePthres: %s" %bluePthres
    
    
    
    if (isRedSum):
        r = red+redNthres
        r[red>redPthres]=255
    else:
        r = red-redNthres
        r[red<redNthres]=0
    if (isGreenSum):
        g = green+greenNthres
        g[green>greenPthres]=255
    else:
        g = green-greenNthres
        g[green<greenNthres]=0
    if(isBlueSum):
        b = blue+blueNthres
        b[blue>bluePthres]=255
    else:
        b = blue-blueNthres
        b[blue<blueNthres]=0
    
    r[r > 255] = 255
    r[r < 0] = 0
    g[g > 255] = 255
    g[g < 0] = 0
    b[b > 255] = 255
    b[b < 0] = 0
    image[:,:,0] = r
    image[:,:,1] = g
    image[:,:,2] = b

    
    imshow(image)
    end_time = time.time()
    runtime = end_time - start_time
    print "Runtime: %s seconds" % runtime
    return image

runCallibration('monk.jpeg','monk2.jpeg','monkcalibrated.jpeg')
