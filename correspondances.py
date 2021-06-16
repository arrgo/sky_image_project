# Can click on the images and store pixel points
# Use to get correspondances between two images

import cv2 as cv

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        cv.circle(img, (x,y), radius=10, color=(0, 0, 255), thickness=-1)
        cv.imshow('image', img)

if __name__ == "__main__":
    img = cv.imread('london_eye.jpg')
    cv.imshow('image', img)
    cv.setMouseCallback('image', click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()

