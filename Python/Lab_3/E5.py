# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:00:38 2016

@author: auort

The cross dissolve method is a modification from stack overflows's cv2 Python 
image blending "Fade" transition accessed at 
http://stackoverflow.com/questions/28650721/cv2-python-image-blending-fade-transition

Write a program to morph a face image in frontal view into another. Use a 
variation of your program from the previous question to align the faces, 
then apply cross-dissolve.

"""

from PIL import Image 
from pylab import *
from numpy import *
import scipy.misc
import cv2
from shutil import copyfile
import time


def warpimage(im, refPt, name):
    newim = zeros(im.shape)
    source = []
    destination = []
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
    inX2 = refPt[0][3]
    inY2 = refPt[0][2]
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
                      newim[int(r)][int(c)] = im[int(newx)][int(newy)]
                  else:
                      newim[r][c] = im[0][0]
    scipy.misc.imsave('warpedimage.jpg', newim)
    scipy.misc.imsave(name, newim)
    
    #imshow(newim)
    
def morphImages():
    imname1 = 'morphim1.jpg'
    imname2 = 'morphim2.jpg'
    
    img1 = Image.open(imname1)
    img2 = Image.open(imname2)
    img2 = img2.resize(img1.size, Image.ANTIALIAS)
    #img2 = resizeimage.resize_thumbnail(img2, img1.size)
    imagewidth = img1.size[0]

    im1 = array(img1)
    im2 = array(img2)
    
    sbsimages = np.concatenate((im1, im2), axis=1)
    imshow(sbsimages)
    
    #imshow(im)
    refPt = ginput(2)
    refPt1 = []
    refPt2 = []
    
    xim1 = refPt[0][0]
    yim1 = refPt[0][1]
    xim2 = refPt[1][0]
    yim2 = refPt[1][1]

    
    if (xim1 > imagewidth):
        xim1 = xim1 - imagewidth
    else:
        xim2 = xim2 - imagewidth
    refPt1.append(([xim1,yim1,xim2,yim2]))
    refPt2.append(([xim2,yim2,xim1,yim1]))
    
    print "morph images called"
    start_time = time.time()
    print "morphing image 1"
    warpimage(im1, refPt1, imname1)
    print "morphing image 2"
    warpimage(im2, refPt2, imname2)
    print "morphing complete"
    end_time = time.time()
    run_time = end_time - start_time
    print run_time

def crossDissolve (im1, im2):
    img1 = array(Image.open(im1).convert('L'))
    img2 = array(Image.open(im2).convert('L'))
    scipy.misc.imsave('crossdisolveCheck1.jpg', img1)
    scipy.misc.imsave('crossdisolveCheck2.jpg', img2)
    #while True:
    for IN in range(0,10):
            fadein = IN/10.0
            dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)#linear $
            cv2.imwrite('crossdisolve'+str(IN)+'.jpg', dst)
            cv2.imshow('window', dst)
            cv2.waitKey(1)
            print fadein
            time.sleep(0.05)
            if fadein == 1.0: #blendmode mover
                    fadein = 1.0
    return # exit function

def runMorphing(name1, name2):
    
    copyfile(name1, 'morphim1.jpg')
    copyfile(name2, 'morphim2.jpg')
    blank = cv2.imread('morphBlank.jpg')
    instructions = cv2.imread('morphInstructions.jpg')
    
    #morphImages()
    morphImages()
    
    
    # keep looping until the 'c' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("instructions", instructions)
        key = cv2.waitKey(1) & 0xFF
        
        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
            break
        elif key == ord("m"):
            cv2.imshow("instructions", blank)
            morphImages()


    # close all open windows
    cv2.destroyAllWindows()

runMorphing('donaldsmall.jpg', 'hillarysmall.jpg')
#crossDissolve ('hillarysmall.jpg','morphim1.jpg')
#crossDissolve ('morphim1.jpg','donaldsmall.jpg')
#crossDissolve ('donaldsmall.jpg','morphim2.jpg')
#crossDissolve ('morphim2.jpg','hillarysmall.jpg')

              