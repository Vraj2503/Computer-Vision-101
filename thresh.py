import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding/Binarizing
threshold , thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)  #Here 150 is the threshold value
cv.imshow('Threshold', thresh)

#Adaptive Thresholding/Binarizing
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive threshold', adaptive_thresh)



cv.waitKey(0)