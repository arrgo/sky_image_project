import cv2 
import numpy as np
from itertools import combinations

def plotter(image, points, color):
    points = np.load(points)
    it = iter(points)

    m = []
    b = []
    for point in it:
        (p1,p2) = (point, next(it))
        x1, y1 = p1[0] + 10000, p1[1] + 100
        x2, y2 = p2[0] + 10000, p2[1] + 100
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


def avg_xy(xys):
    x_vals = 0
    y_vals = 0
    tot = len(xys)
    for tup in xys:
        x, y = tup 
        x_vals += x
        y_vals += y 
    return x_vals/ tot, y_vals/tot

def RANSAC_pts(points, error):
    points = np.load(points)
    it = iter(points)

    m = []
    b = []
    for point in it:
        (p1,p2) = (point, next(it))
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        if(x2 - x1 != 0):
            slope = (y2-y1) / (x2-x1)
            inter = y2 - slope*x2
            m.append(slope)
            b.append(inter)

    length = len(m)
    numbers = range(length)
    choose2 = combinations(numbers, 2)
    intersections = []
    #from each combination of two lines, get the point of intersection
    for comb in choose2:
        ind1, ind2 = comb
        y_int = (b[ind1] - (m[ind1] * b[ind2] / m[ind2])) / (1 - (m[ind1]/m[ind2]))
        x_int = (y_int - b[ind1]) / m[ind1]
        intersections.append((x_int, y_int))

    #RANSAC on each point of intersection
    max_inliers = 0
    best_inter = -1
    inter_list = []
    for inter in intersections:
        inliers = 0
        #print(inter)
        for other_inter in intersections:
            #print(np.linalg.norm(np.array(inter) - np.array(other_inter)))
            if other_inter == inter:
                pass
            elif np.linalg.norm(np.array(inter) - np.array(other_inter)) < error:
                inliers += 1
        
        #print("inliers = " + str(inliers))
          
        if inliers == max_inliers:
            inter_list.append(inter)
            
        if inliers > max_inliers:
            max_inliers = inliers
            inter_list = []
            inter_list.append(inter)
            best_inter = inter
    
    
    print(f'inliers: {max_inliers} out of {len(intersections)}, for which there were {len(inter_list)} matches')   
    return avg_xy(inter_list) 

    



if __name__ == "__main__":
    print(RANSAC_pts('westminister_diagonal.npy', 50))
    
    image = cv2.imread('westminister.jpg')
    image = cv2.copyMakeBorder(image, 100, 10000, 10000, 10000, cv2.BORDER_CONSTANT)

    image = plotter(image, 'westminister_horizontal.npy', (0, 255, 0))    
    image = plotter(image, 'westminister_diagonal.npy', (0, 255, 0))  
    image = plotter(image, 'westminister_vertical.npy', (0, 255, 0))    
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

