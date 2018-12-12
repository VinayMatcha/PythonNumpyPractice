import numpy as np


a = np.array([[1,1],[1.5, 4]])
b = np.array([2200, 5050])
x = np.linalg.solve(a, b)
print(x[0], "children and", x[1], "adults")