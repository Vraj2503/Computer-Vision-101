import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Image', img)

#GrayScale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)
#Can reduce the amount of edges by passing the blur image as the image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#Eroded image 
#Same syntax, take the dilated image as the input

#Resize
#Same Syntax, But resizig ignores the aspect ratio

#Crop




cv.waitKey(0)