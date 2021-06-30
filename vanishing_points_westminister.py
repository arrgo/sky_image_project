import cv2 
import numpy as np

def plotter(image, points, color):
    points = np.load(points)
    it = iter(points)

    m = []
    b = []
    for point in it:
        (p1,p2) = (point, next(it))
        x1, y1 = p1[0] + 500, p1[1] + 100
        x2, y2 = p2[0] + 500, p2[1] + 100
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
    image = cv2.imread('westminister.jpg')
    image = cv2.copyMakeBorder(image, 100, 100, 500, 10000, cv2.BORDER_CONSTANT)
    
    image = plotter(image, 'westminister_horizontal.npy', (0, 255, 0))    
    image = plotter(image, 'westminister_diagonal.npy', (0, 255, 0))    
    cv2.imshow("westminister_intersections", image) 
    cv2.setMouseCallback('westminister_intersections', click_event)
    cv2.waitKey(0)



    """"points = np.load('westminister_vertical.npy')
    it = iter(points)
    m = []
    b = []
    for point in it:
        (p1,p2) = (point, next(it))
        x1, y1 = p1[0] + 500, p1[1] + 100
        x2, y2 = p2[0] + 500, p2[1] + 100
        if(x2 - x1 != 0):
            slope = (y2-y1) / (x2-x1)
            m.append(slope)
            b.append(y2 - slope*x2)
            #m = (y2-y1) / (x2-x1)
            #b = y2 - m*x2
            # y = mx + b
    print(np.shape(m))
    print(np.shape(b))
    print(m)
    print(b)"""

