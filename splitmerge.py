import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Image', img)

#Split Image
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
#The lighter the portion in the image, the more is the concentration of the color in the portion

#Merge
Img = cv.merge([b,g,r])
cv.imshow('Merged', Img)

#Another way to represent the merge
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)




cv.waitKey(0)