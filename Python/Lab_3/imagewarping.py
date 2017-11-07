# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:00:38 2016

@author: Rebecca
"""

from PIL import Image 
from pylab import *
from numpy import *

source = []
destination = []
im = array(Image.open('hillary.jpg'))
newim = zeros(im.shape)
imshow(im)
inpu = ginput(2)

#corner points
source.append([0,0])
source.append([0,len(im[0])])
source.append([len(im),0])
source.append([len(im),len(im[0])])

destination.append([0,0])
destination.append([0,len(im[0])])
destination.append([len(im),0])
destination.append([len(im),len(im[0])])

#ginput recieves coordinates as y,x
inX = inpu[0][1]
inY = inpu[0][0]
source.append([inX,inY])

inX2 = inpu[1][1]
inY2 = inpu[1][0]
destination.append([inX2,inY2])

#Added by Angel
disp = subtract(source, destination)

weight = []#array(im.shape)
for r in range(len(im)):
   for c in range(len(im[0])):
       distance = zeros(len(destination))
       for dest in range(len(destination)):
              distance[dest] = (sqrt(pow(r-destination[dest][0],2) + pow(c-destination[dest][1],2)))
              #print " "
              weight = 1/(distance + 0.0000001)
              weight = weight/sum(weight)
              newx = r + dot(weight, disp)[0]
              newy = c +dot(weight, disp)[1]
              '''
              print (newx, newy)
              print("~~~~")
              '''
              if (newx < len(im)-1 and newy < len(im[0])-1):
                  newim[r][c] = im[newx][newy]
              else:
                  newim[r][c] = im[0][0]
scipy.misc.imsave('warped.jpg', newim)
imshow(newim)
              