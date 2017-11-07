# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:05:13 2016

@author: auort
"""
from PIL import Image
import numpy as np
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

def replaceImage(coordinateArray, sourceimage, image):
    height = len(coordinateArray[0])
    width = len(coordinateArray)
    for y in range(height):
        for x in range(width):
            '''
            print "x: %d, y: %d" % (x,y)
            print "width: %d, height: %d" % (width,height)
            '''
            xcoor = int(coordinateArray[x][y][0])
            ycoor = int(coordinateArray[x][y][1])
            try:
                image[ycoor][xcoor] = sourceimage[x][y]
            except IndexError:
                print "Index Error caught"
    return image
    
def resizeimagetoarray(image, width, length):
    image = Image.open(image)
    image = image.resize((width,length))
    return np.array(image)
    
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
    
def runImageReplace(Source, Destination):
    image = np.array(Image.open(Source))
    dest = np.array(Image.open(Destination))
    Ax,Ay,Bx,By,Cx,Cy,Dx,Dy = getCorners(dest)
    start_time = time.time()
    print "Getting Coordinate Array"
    coordinateArray = getCoordinateArray(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy)
    width, length = getMaxWidthAndHeight(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy)
    print "Resizing source image"
    sourceimage = resizeimagetoarray(Source, width, length)
    scipy.misc.imsave('resizedsource.jpg', sourceimage)
    print "replacing image"
    imageReplaced = replaceImage(coordinateArray, sourceimage, dest)
    print type(imageReplaced)
    #imageReplaced.save('replacedcover.jpg')
    scipy.misc.imsave('replacedcover2.jpg', imageReplaced)
    
    
    print "image has been saved"
    end_time = time.time()
    print "Run Time: %s" % (end_time - start_time)
    
runImageReplace('donald.jpg','book.jpg')