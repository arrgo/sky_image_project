import cv2
import numpy as np
from scipy.spatial import distance
from scipy.linalg import null_space, cholesky

def get_slope_inter(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1 
    return (m, b)

def get_perp_point(slope, x , y):
    #slope of perpendicular line, point on line
    m = -1 / slope 
    #y = mx + b
    b = y - (m * x)
    return (m, b)

def get_intersect(m1, b1, m2, b2):
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)


def plot_triangle(image, p1, p2, p3, name):
    image = cv2.circle(image, p1, radius=30, color=(0, 0, 255), thickness= -1)
    image = cv2.circle(image, p2, radius=30, color=(0, 255, 0), thickness= -1)
    image = cv2.circle(image, p3, radius=30, color=(255, 0, 0), thickness= -1)
    
    #line 1
    m1, b1 = get_slope_inter(p1[0], p1[1], p2[0], p2[1])
    image = cv2.line(image, (p1[0], int(m1*p1[0] + b1)), (p2[0], int(m1*p2[0]+b1)), (0, 0, 255), 3) 
    
    #line 2
    m2, b2 = get_slope_inter(p1[0], p1[1], p3[0], p3[1])
    image = cv2.line(image, (p1[0], int(m2*p1[0] + b2)), (p3[0], int(m2*p3[0]+b2)), (0, 0, 255), 3) 
    
    #line 2
    m3, b3 = get_slope_inter(p2[0], p2[1], p3[0], p3[1])
    image = cv2.line(image, (p2[0], int(m3*p2[0] + b3)), (p3[0], int(m3*p3[0]+b3)), (0, 0, 255), 3) 

    #--- perpendiculars:
    m4, b4 = get_perp_point(m1, p3[0], p3[1])
    m5, b5 = get_perp_point(m2, p2[0], p2[1])
   
    image = cv2.line(image, (p3[0], int(m4*p3[0] + b4)), (p3[0] + 1000, int(m4*(p3[0] + 1000)+b4)), (0, 0, 255), 3) 
    image = cv2.line(image, (p2[0], int(m5*p2[0] + b5)), (p2[0] + 1000, int(m5*(p2[0] + 1000)+b5)), (0, 0, 255), 3) 

    x, y = get_intersect(m4, b4, m5, b5)
    print(f"{name} orthocenter")
    print((int(x),int(y)))
    image = cv2.circle(image, (int(x), int(y)), radius=30, color=(255, 255, 255), thickness= -1)
    
    cv2.imshow('image', image)
    cv2.waitKey(0)

    return x, y

def get_vp_constraints(u, v):
    #https://github.com/carlosbeltran/EyeLib/blob/master/matlab/computeKviaIAC.m
    a = [v[0]*u[0]+v[1]*u[1],
     u[0]+v[0],
     u[1]+v[1],
     1]
    return a

def get_A(v1, v2, v3):
    a1 = get_vp_constraints(v1, v2)
    a2 = get_vp_constraints(v1, v3)
    a3 = get_vp_constraints(v2, v3)

    A = np.vstack((a1, a2, a3))
    return A 

if __name__ == "__main__":
    p1 = (1861, 5577) #horiz y
    p2 = (10355, 5659) #vert z
    p3 = (1939, 1366) #diag x
    image = cv2.imread('london_eye.jpg')
    image = cv2.copyMakeBorder(image, 5000, 1000, 1000, 9000, cv2.BORDER_CONSTANT)
    lex, ley = plot_triangle(image, p1, p2, p3, "london_eye.jpg")

    p1 = (11262, 585)
    p2 = (5116, 679)
    p3 = (10995, 11735)
    image = cv2.imread("westminister.jpg")
    image = cv2.copyMakeBorder(image, 100, 11000, 10000, 10000, cv2.BORDER_CONSTANT)
    wx, wy = plot_triangle(image, p1, p2, p3, "westminister.jpg")

    x_le = distance.euclidean((lex, ley), p3)
    y_le = distance.euclidean((lex, ley), p1)
    z_le = distance.euclidean((lex, ley), p2)

    x_w = distance.euclidean((wx, wy), p3)
    y_w = distance.euclidean((wx, wy), p1)
    z_w = distance.euclidean((wx, wy), p2)

    """
    #London Eye Vanishing Points
    v1_le = [x_le, 0, 0]
    v2_le = [0, y_le, 0]
    v3_le = [0, 0, z_le]

    #Westminister Vanishing Points
    v1_w = [x_w, 0, 0]
    v2_w = [0, y_w, 0]
    v3_w = [0, 0, z_w]
    """
    """
    #London Eye Vanishing Points
    v1_le = [4319, 944, 1]
    v2_le = [1013,  -3060, 1]
    v3_le = [873, 647, 1]

    #Westminister Vanishing Points
    v1_w = [8551, 1022, 1]
    v2_w = [1260, 503, 1]
    v3_w = [1115, 11946, 1]

    A_le = get_A(v1_le, v2_le, v3_le)
    A_w = get_A(v1_w, v2_w, v3_w)

    #w_le = null_space(A_le) #use SVD pick last row of VT
    #W = [ w(1) 0 w(2);0 w(1) w(3);w(2) w(3) w(4)];
    U, S, Vh = np.linalg.svd(A_le)
    print(U)
    print(S)
    print(Vh)
    w_le = Vh[3, :].T
    

    print(w_le)
    print(null_space(A_le))
    
    W_le = [ [w_le[0], 0, w_le[1]],
        [0, w_le[0], w_le[2]],
        [w_le[1], w_le[2], w_le[3]] ]
    W_le = np.matrix(W_le, dtype='float')
    print(W_le)
    print(np.linalg.inv(W_le))
    print(np.linalg.cholesky(np.linalg.inv(W_le)))
    #K_le = np.linalg.inv(np.linalg.cholesky(W_le))
    #print(K_le)
    """
    """
    w_w= null_space(A_w)
    W_w = [ [w_w[0], 0, w_w[1]],
        [0, w_w[0], w_w[2]],
        [w_w[1], w_w[2], w_w[3]] ]
    W_w = np.matrix(W_le, dtype='float')
    K_w = np.linalg.inv(np.linalg.cholesky(W_le))

    """

    

