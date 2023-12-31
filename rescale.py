import cv2 as cv

#Reading Images
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)


def rescaleframe(frame, scale=0.2):
    #Images, Videos and Live Video
    width = int(frame.shape[0]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    #Only Live Video
    capture.set(3, width)
    capture.set(4, height)




# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleframe(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)




