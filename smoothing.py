import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Image', img)

#Average Blur
avg = cv.blur(img, (3,3))
cv.imshow('Average Blur', avg)
#It finds the average between the neighbouring pixels 

#Median Blur
mdn = cv.medianBlur(img, 3)
cv.imshow('Median BLur', mdn)
#It finds the median between the neighbouring pixels

#Gaussian Blur
guass = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Guassian Blur', guass)
#Its more natural blurring 

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)
#It keeps the edges unblurred
#It works best with lower kernel sizes


cv.waitKey(0)