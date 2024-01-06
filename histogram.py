import cv2 as cv 
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
>>>>>>> 340def66ebfca45f018edfbcd3ca4b11bdb7e6bb

img = cv.imread("Photos/cats.jpg")
cv.imshow("Image", img)

<<<<<<< HEAD
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
=======


>>>>>>> 340def66ebfca45f018edfbcd3ca4b11bdb7e6bb


cv.waitKey(0)