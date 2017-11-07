# -*- coding: utf-8 -*-
"""
Created on Sat Oct 8 12:34:18 2016

@author: auort

The image point selection part of this program was derived from Adrian 
Rosebrock's Capturing mouse click events with Python and OpenCV, available at
http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-
python-and-opencv/

Write a program to implement k-nearest neighbor warping, as explained in class. 
Your program should allow the user to input source and destination points and 
generate a sequence of images illustrating a smooth transition from the source 
to the destination image. 

"""
import cv2 
import numpy as np
import math
import pylab
import copy
import time

# initialize the list of reference points and boolean indicating
# whether selecting is being performed or not
refPt = []
selecting = False
 
def click_and_save(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, selecting
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
         refPt = [(x, y)]
         selecting = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
         refPt.append((x, y))
         
         selecting = False
         # draw a line between two points
         display = cv2.imread('warpedimage.jpg')
         original = cv2.imread('warpedimage.jpg')
         #warp(display, refPt)
         cv2.line(display, refPt[0], refPt[1], (0, 255, 0), 2)
         cv2.imshow("image selection", display)
         cv2.imwrite('warpedimageselection.jpg', display)
         warp(refPt)
         display = cv2.imread('warpedimage.jpg')
         cv2.imshow("warped image", display)
    
def warp(refPt):
    #print "warping image"
    start_time = time.time()
    source = []
    destination = []
    im = array(Image.open('warpedimage.jpg'))
    newim = zeros(im.shape)
    
    #corner points
    source.append([0,0])
    source.append([0,len(im[0])])
    source.append([len(im),0])
    source.append([len(im),len(im[0])])
    destination.append([0,0])
    destination.append([0,len(im[0])])
    destination.append([len(im),0])
    destination.append([len(im),len(im[0])])
    
    inX = refPt[0][1]
    inY = refPt[0][0]
    source.append([inX,inY])
    inX2 = refPt[1][1]
    inY2 = refPt[1][0]
    destination.append([inX2,inY2])
    
    disp = subtract(source, destination)
    weight = []
    
    for r in range(len(im)):
       for c in range(len(im[0])):
           distance = zeros(len(destination))
           for dest in range(len(destination)):
                  distance[dest] = (sqrt(pow(r-destination[dest][0],2) + pow(c-destination[dest][1],2)))
                  weight = 1/(distance + 0.0000001)
                  weight = weight/sum(weight)
                  newx = r + dot(weight, disp)[0]
                  newy = c +dot(weight, disp)[1]
                  if (newx < len(im)-1 and newy < len(im[0])-1):
                      newim[r][c] = im[int(newx)][int(newy)]
                  else:
                      newim[r][c] = im[0][0]
    scipy.misc.imsave('warpedimage.jpg', newim)
    end_time = time.time()
    print "Run Time: %s" % (end_time - start_time)
    
def runSelectiveWarping(Path):
    image = cv2.imread(Path)
    cv2.imwrite('warpedimage.jpg', image)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_save)
     
    # keep looping until the 'c' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
            break
        elif key == ord("n"):
            runSelectiveWarping('warpedimage.jpg')
    # close all open windows
    cv2.destroyAllWindows()
    
Path = 'monica1.jpg'
runSelectiveWarping(Path)
