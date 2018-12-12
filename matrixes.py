import numpy as np

#must be same size in every row
mat = np.array([[1,2],[3,4]])

print(mat[0][0], mat[0,0])
mat1 = [[1,2],[3,4]]

mat2 = np.matrix([[1,2],[3,4]])
mat2 = np.array(mat2)
mat2 = mat2.T
print(mat2)

Z = np.zeros(20)
print(Z)
Z1 = np.zeros((10,10))
print(Z1)
Z2 = np.ones((10,10))

#normla distribution between 0 to 1
ran = np.random.random((10,10))

#gaussian with mean 0 and variance 1
ranGau = np.random.randn(10,10)
print(ranGau)
