import cv2 
import numpy as np

def plotter(image, points, color):
    points = np.load(points)
    it = iter(points)

    m = []
    b = []
    for point in it:
        (p1,p2) = (point, next(it))
        x1, y1 = p1[0] + 1000, p1[1] + 5000
        x2, y2 = p2[0] + 1000, p2[1] + 5000
        if(x2 - x1 != 0):
            #slope = (y2-y1) / (x2-x1)
            #m.append(slope)
            #b.append(y2 - slope*x2)
            m = (y2-y1) / (x2-x1)
            b = y2 - m*x2
            # y = mx + b
            image = cv2.line(image, (0, int(b)), (19000, int(m*19000+b)), color, 3)

    return image

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        cv2.circle(image, (x,y), radius=10, color=(0, 0, 255), thickness= -1)
        cv2.imshow('image', image)

if __name__ == "__main__":
    image = cv2.imread('london_eye.jpg')
    image = cv2.copyMakeBorder(image, 5000, 1000, 1000, 5000, cv2.BORDER_CONSTANT)
    image = plotter(image, 'london_eye_vertical.npy', (0, 255, 0))    
    image = plotter(image, 'london_eye_horizontal.npy', (0, 0, 255)) 
    image = plotter(image, 'london_eye_diagonal.npy', (255, 0, 0)) 
    cv2.imshow("london_eye_intersections", image) 
    cv2.setMouseCallback('london_eye_intersections', click_event)
    cv2.waitKey(0)