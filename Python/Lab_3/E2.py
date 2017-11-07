# -*- coding: utf-8 -*-
"""
Created on Sun Oct 2 15:58:58 2016

@author: auort

Write a program to extract the image of a rectangular object seen under 
perspective in an image and display it without perspective effects. You can 
do this using the homography-based algorithm described in the textbook, or 
the line-based algorithm described in class. 

"""

import numpy as np
from PIL import Image
import scipy.misc
import time
from pylab import *
from numpy import *


    
def getMaxWidthAndHeight(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    width1 = abs(Bx-Ax)
    width2 = abs(Cx-Dx)
    height1 = abs(Dy-Ay)
    height2 = abs(Cy-By)
    return int(max(width1, width2)), int(max(height1, height2))

def getValues(A, B, index, partitions):
    Ax = A[0]
    Ay = A[1]
    Bx = B[0]
    By = B[1]
    '''
    print "Ax: %d, Ay: %d, Bx: %d, By: %d " % (Ax, Ay, Bx, By)
    '''
    width = abs(Bx-Ax)
    height = abs(By-Ay)
    stepup = float(height)/partitions
    stepover = float(width)/partitions
    '''
    print "Width: %s" % width
    print "Height: %s" % height
    '''
    if(Ax > Bx):
        stepover = stepover *-1
    ''''
    print "Stepup: %s" % stepup
    print "Stepover: %s" % stepover
    print "Partitions: %s" % partitions
    '''
    xvalue = Ax + (stepover*index)
    yvalue = Ay + (stepup*index)
    return [xvalue,yvalue]
    
    
def getCoordinateArray(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    width, height =  getMaxWidthAndHeight(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
    array = []
    leftcolumn = []
    rightcolumn = []
    '''
    print Ax
    print Ay
    print Dx
    print Dy
    print height  
    '''
    #print "-----------------------------building columns: "
    leftcolumn = [getValues([Ax, Ay], [Dx, Dy], 0, height)]
    #print leftcolumn
    rightcolumn = [getValues([Bx, By], [Cx, Cy], 0, height)]
    #print rightcolumn
    for i in range(height-1):
        #print i
        leftcolumn.append(getValues([Ax, Ay], [Dx, Dy], i+1, height))
        rightcolumn.append(getValues([Bx, By], [Cx, Cy], i+1, height))
        i=i
    '''
    print "-----------------------------printing leftcolumn: "
    print leftcolumn
    print "-----------------------------printing rightcolumn: "
    print rightcolumn
    
    print "-----------------------------buiding array: "
    '''
    coordinatearray = []
    row = []
    for y in range(height):
        for x in range(width):
            value = getValues(leftcolumn[y], rightcolumn[y], x, width)
            row.append(value)
            '''
            print " "
            print "leftcolumn[y]:"
            print leftcolumn[y]
            print "rightcolumn[y]:"
            print rightcolumn[y]
            print "value:"
            print value
            '''
        coordinatearray.append(row)
        row = []
        
    return coordinatearray

def extractImage(coordinateArray, image):
    print "Extract image called"
    width = len(coordinateArray)
    height = len(coordinateArray[0])
    extractedImage = []
    row = []
    for y in range(height):
        for x in range(width):
            print x
            print y
            row.append(pixelcoloraverage(coordinateArray[x][y], image))
        extractedImage.insert(0, row)
        row = []
        
    return extractedImage

def getCorners(image):
    imshow(image)
    refPt = ginput(4)
    Ax = refPt[0][0]
    Ay = refPt[0][1]
    Bx = refPt[1][0]
    By = refPt[1][1]
    Cx = refPt[2][0]
    Cy = refPt[2][1]
    Dx = refPt[3][0]
    Dy = refPt[3][1]
    close()
    return Ax, Ay, Bx, By, Cx, Cy, Dx, Dy  
    
def runImageExtraction(Path, Path2):
    image = np.array(Image.open(Path))
    Ax,Ay,Bx,By,Cx,Cy,Dx,Dy = getCorners(image)
    start_time = time.time()
    
    coordinateArray = getCoordinateArray(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy)
    h = len(coordinateArray[0])
    w = len(coordinateArray)
    '''
    print "Height: %s" % h
    print "Width: %s" % w
    print "A: %d, %d" %(coordinateArray[0][0][0], coordinateArray[0][0][1])
    print "B: %d, %d" %(coordinateArray[w-1][0][0], coordinateArray[w-1][0][1])
    print "C: %d, %d" %(coordinateArray[w-1][h-1][0], coordinateArray[w-1][h-1][1])
    print "D: %d, %d" %(coordinateArray[0][h-1][0], coordinateArray[0][h-1][1])
    '''
    #print "---------------------------Coordinate Array:"
    #print coordinateArray
    imageExtracted = extractImage(coordinateArray, image)
    scipy.misc.imsave(Path2, imageExtracted)
    imageExtracted = np.rot90(imageExtracted,3)
    scipy.misc.imsave(Path2, imageExtracted)
    
    print "image has been saved"
    end_time = time.time()
    print "Run Time: %s" % (end_time - start_time)
    
runImageExtraction('maiko2.jpg','maikoextracted.jpg')

