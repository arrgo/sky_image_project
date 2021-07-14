import numpy as np
from triangle import get_A

#westmin
v1 = (1262, 485, 1)
v2 = (-4884, 579, 1)
v3 = (995, 11635, 1)

#london eye
"""v1 = (861, 577, 1)
v2 = (9355, 659, 1)
v3 = (932, -3634, 1)"""



A = get_A(v1, v2, v3)
U, S, Vh = np.linalg.svd(A)
w_le = Vh[3, :].T

W_le = [ [w_le[0], 0, w_le[1]],
        [0, w_le[0], w_le[2]],
        [w_le[1], w_le[2], w_le[3]] ]
W_le = np.matrix(W_le, dtype='float')
chol = np.linalg.cholesky(W_le)
inv = np.linalg.inv(chol)
print((inv/inv[2, 2]).astype(int).T)


"""
K (intrinsic) results:

LE: 
[[503, 0, 891],
[0, 503, 516],
[0, 0,  1]]

Westmin
[[1564, 0, 827],
[0, 1564, 615], 
[0, 0, 1]]
"""