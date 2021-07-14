import numpy as np
from triangle import get_A

#westmin
"""v1 = (8551, 1022, 1)
v2 = (1260, 503, 1)
v3 = (1115, 11946, 1)"""

#london eye
v1 = (4319, 855, 1)
v2 = (1100,  -3060, 1)
v3 = (873, 647, 1)



A = get_A(v1, v2, v3)
U, S, Vh = np.linalg.svd(A)
w_le = Vh[3, :].T
"""W_le = [ [w_le[0], 0, w_le[1]/1.65],
        [0, w_le[0], w_le[2]/1.65],
        [w_le[1]/1.65, w_le[2]/1.65, w_le[3]] ]"""

W_le = [ [w_le[0], 0, w_le[1]],
        [0, w_le[0], w_le[2]],
        [w_le[1], w_le[2], w_le[3]] ]
W_le = np.matrix(W_le, dtype='float')
print(W_le)
chol = np.linalg.cholesky(W_le)
inv = np.linalg.inv(chol)
print((inv/inv[2, 2]).astype(int).T)


"""
K (intrinsic) results:

LE: 
[[105, 0, 876],
[0, 105, 644],
[0, 0,  1]]

Westmin
[[2070, 0, 1898],
[0, 2070, 937], 
[0, 0, 1]]
"""