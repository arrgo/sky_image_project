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
    img = cv.imread('hilton_pl.jpg')
    cv.imshow('image', img)
    cv.setMouseCallback('image', click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(np.shape(points))
    np.save('hilton_pl_vertical', points)

