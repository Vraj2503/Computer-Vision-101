import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("Image", img)

#GrayScale Histogram
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
#Can also be done for masked images


#Color Histogram
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
    
plt.show()


cv.waitKey(0)