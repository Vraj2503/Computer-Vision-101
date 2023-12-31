import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Image', img)

gray = cv.imread('Photos/cats.jpg', 0)
cv.imshow('Gray', gray)

#Can be done like this as well
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', gray)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', threshold)   #This function works in binary, i.e, its either 125 or 255(black or white)

contours, heirarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

#Drawing the contours of the image 

blank = np.zeros(img.shape, dtype='uint8')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours Drawn", blank)

#From this method we know that the generated image is not the same as the canny image as contours and edges are considered differently
#If we want them to be the same then use the input image as canny and dont use threshold


cv.waitKey(0)