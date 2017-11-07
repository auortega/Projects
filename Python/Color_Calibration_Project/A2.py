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
import copy
import cv2
import scipy
    
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

def runPassportCallibrations(Path1, Path2):
    thresholds = np.zeros((24,9))
    for i in range(24):
        showColor = getSelection(Path1)
        trueColor = getSelection(Path2)
        thresholds[i]=getThres(trueColor, showColor)
    #print thresholds

def getThres(trueColor, showColor):
    rT = trueColor[0]
    gT = trueColor[1]
    bT = trueColor[2]
    rS = showColor[0]
    gS = showColor[1]
    bS = showColor[2]
    
    isRedSum = (trueColor[0]>showColor[0])
    isGreenSum = (trueColor[1]>showColor[1])
    isBlueSum = (trueColor[2]>showColor[2])
    
    rabsdif = abs(rT-rS)
    gabsdif = abs(gT-gS)
    babsdif = abs(bT-bS)
    if (not(isRedSum)):
        rabsdif = 255-rabsdif
    if (not(isGreenSum)):
        gabsdif = 255-gabsdif
    if (not(isBlueSum)):
        babsdif = 255-babsdif

    redNthres = rabsdif
    greenNthres = gabsdif
    blueNthres = babsdif
    
    redPthres = 255-rabsdif
    greenPthres = 255-gabsdif
    bluePthres = 255-babsdif
    
    if(redPthres<redNthres):
        temp = redPthres
        redPthres=redNthres
        redNthres=temp
    if(greenPthres<greenNthres):
        temp=greenPthres
        greenPthres=greenNthres
        greenNthres=temp
    if(bluePthres<blueNthres):
        temp=bluePthres
        bluePthres=blueNthres
        blueNthres=temp

    return redNthres, greenNthres, blueNthres, redPthres, greenPthres, bluePthres, isRedSum, isGreenSum, isBlueSum

def createCallibratedImage(Path, values):
    start_time = time.time()
    
    image = np.array(Image.open(Path))
    
    redNthres = values[0]
    greenNthres = values[1]
    blueNthres = values[2]
    redPthres = values[3]
    greenPthres = values[4]
    bluePthres = values[5]
    isRedSum = values[6]
    isGreenSum = values[7]
    isBlueSum = values[8]
    
    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
    
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
    
    end_time = time.time()
    runtime = end_time - start_time
    print "Runtime of Image Callibration: %s seconds" % runtime
    return image    
    
def getPassportCoords(Path):
    image = np.array(Image.open(Path))
    imshow(image)
    refPt = ginput(2)
    close()
    pointI = refPt[0]
    
    Ix = int(pointI[0])
    Iy = int(pointI[1])
    pointF = refPt[1]
    
    Fx = int(pointF[0])
    Fy = int(pointF[1])
  
    #coordsv = np.zeros((24,2))
    coordsa = np.zeros((6,4,2))
    colors = np.zeros((6,4,3))
    for i in range (6):
        x = 0
        y = 0
        width = Fx-Ix
        height = Fy-Iy
        x = (width/5)* i + Ix
        for j in range(4):
            y = (height/3)* j +Iy
            coordsa[i][j][0]=x
            coordsa[i][j][1]=y
            colors[i][j][0]=image[y][x][0]
            colors[i][j][1]=image[y][x][1]
            colors[i][j][2]=image[y][x][2]
            
    return coordsa, colors

def getPassportsColorDifference(Path1, Path2):
    coorA, colorA = getPassportCoords(Path1)
    coorB, colorB = getPassportCoords(Path2)
    pCD = np.zeros((6,4,9))#passportColorDifference
    for i in range(6):
        for j in range(4):
            pCD[i][j][0],pCD[i][j][1],pCD[i][j][2],pCD[i][j][3],pCD[i][j][4],pCD[i][j][5],pCD[i][j][6],pCD[i][j][7],pCD[i][j][8]=getThres(colorB[i][j], colorA[i][j])
    
    #print "Finished getting passports' color difference"
    return pCD, colorA
    
def getimage(array, label, img):
    #print "getting image for posterize"
    array = np.uint8(array)#convert from float to int
    result = array[label.flatten()]

    resultimage = result.reshape((img.shape))#convert to original shape
    height = len(img)
    width = len(img[0])
    indeximage = np.zeros((height, width))
    #print "creating indeximage"
    for i in range (len(resultimage)):
        for j in  range (len(resultimage[0])):
            for k in range (len(array)):
                if (array[k][0]==resultimage[i][j][0] and array[k][1]==resultimage[i][j][1] and array[k][2]==resultimage[i][j][2]):
                    indeximage[i][j]=k
    return resultimage, array, indeximage

def posterize(imagename, numcolors, savedirectory):
    #print "Posterize called!"
    img = cv2.imread(imagename)
    #img2 = cv2.imread("//utep//passport.jpg")
    array = img.reshape((-1,3))
    array = np.float32(array) #cv2.kmeans needs float array, soarray must be converted
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)#stop iteration if epsilon is reached or if max iterations has occured; max iterations = 10, epsilon = 1.0
    ret,label,result=cv2.kmeans(array, numcolors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    resultimage, colors, indeximage = getimage(result, label, img)
    cv2.imwrite(savedirectory, resultimage)
    #print "returning from posterize"
    return colors, indeximage
    
def runmulticalibration(Path1, Path2, Image, n, SaveDir):
    starttime = time.time()
    stime = time.time()
    pCD, pcolors = getPassportsColorDifference(Path1, Path2)
    etime = time.time()
    print "Runtime for getPassportsColorDifference: %s seconds" % (etime-stime)
    #print "Calling posterize..."
    stime = time.time()
    icolors, indeximage = posterize(Image, n, 'temporaryposter.jpg')
    etime = time.time()
    print "Runtime for posterize: %s seconds" % (etime-stime)
    #print "len(icolors) should be 2: %s" % len(icolors)
    indexes = np.zeros((len(icolors),2))
    #print "Entering nested for loop!"
    stime = time.time()
    
    for i in range (len(icolors)):
        indexes[i][0]=0
        indexes[i][1]=0
        value=254*3
        for j in range (len(pcolors)):
            for k in  range (len(pcolors[0])):
            
                red = abs(abs(icolors[i][0])-abs(pcolors[j][k][0]))
                green = abs(abs(icolors[i][1])-abs(pcolors[j][k][1]))
                blue = abs(abs(icolors[i][2])-abs(pcolors[j][k][2]))
                difference = red+green+blue
            
            
            difference = abs(red)+abs(green)+ abs(blue)
            #print "difference: %s" % difference
            
            if (difference < value):
                #print "new smaller difference"
                value = difference
                indexes[i][0] = j
                indexes[i][1] = k
                #print indexes[i]
    
    etime = time.time()
    print "Runtime for nearest neighbor: %s seconds" % (etime-stime)
    
    stime = time.time()
    #print "Starting calibrated image creation"
    
    calibratedimages = np.zeros((n, len(indeximage), len(indeximage[0]), 3))
    
    for i in range(n):
        identifier = str(i)
        x = indexes[i][0]
        y = indexes[i][1]
        image = createCallibratedImage(Image, pCD[x][y])
        calibratedimages[i]=image
        name = "calibratedimage" + identifier + ".jpg"
        scipy.misc.imsave(name, image)
        #imshow(image)
   
    length = len(indeximage)
    width = len(indeximage[0])
    finalimage = np.zeros((length,width, 3))
    for i in range (len(indeximage)):
        #print "running loop... %s /%s" % i, length
        for j in range (len(indeximage[0])):
            index = indeximage[i][j]
            finalimage[i][j][0] = calibratedimages[index][i][j][0]
            finalimage[i][j][1] = calibratedimages[index][i][j][1]
            finalimage[i][j][2] = calibratedimages[index][i][j][2]
    #imshow(finalimage)
    scipy.misc.imsave(SaveDir, finalimage)
    endtime = time.time()
    print "Total runtime: %s seconds" % (endtime-starttime)

runmulticalibration('IMG_0232.jpg','passportlarge.jpg','IMG_0233.jpg',5,'FinalCalibratedImage.jpg')
