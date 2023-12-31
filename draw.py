import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain color 

#Paint the full screen
# blank[:] = 0,0,255
# cv.imshow('Red', blank)

#Paint a certain portion
# blank[300:400, 300:400] = 0,0,255
# cv.imshow('Red', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness = 2)
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness = -1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
#Similar syntax

# 4. Draw a line
#Similar Syntax

# 5. Write Text

cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)