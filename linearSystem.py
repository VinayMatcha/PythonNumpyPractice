import numpy as np

#finding Ax = b. we have to find x
a =  np.array([[1,2],[3,4]])
b = np.array([3,4])
x = np.linalg.inv(a).dot(b)
print(x)
print(a.dot(x))
x = np.linalg.solve(a, b)
print(x)