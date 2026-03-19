import numpy as np

u = np.array([3, 2])
v = np.array([1, -1])
w = np.array([5, 1])

A = np.column_stack((u, v))

a, b = np.linalg.solve(A, w)

print("Os valores de a e b são:", a, b)