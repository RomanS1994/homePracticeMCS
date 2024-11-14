import numpy as np

A = np.array([[1, -2, 3], [1, -2, 2], [-2, 0, 1]])

res = np.linalg.det(A)
print(round(res))