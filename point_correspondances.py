import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html

"""
img2 = cv.imread('london_eye.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
img1 = cv.imread('westminister.jpg',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
print(np.shape(matches))
# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:3], None, flags=0)
plt.imshow(img3),plt.show()

"""

# Can click on the images and store pixel points
# Use to get correspondances between two images

import cv2 as cv
import numpy as np

points = []

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        points.append((x,y))
        cv.circle(img, (x,y), radius=10, color=(0, 0, 255), thickness= -1)
        cv.imshow('image', img)

if __name__ == "__main__":
    img = cv.imread('london_eye.jpg')
    cv.imshow('image', img)
    cv.setMouseCallback('image', click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(np.shape(points))
