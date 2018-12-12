import numpy as np

A = np.array([[1,2],[3,4]])

Ainv = np.linalg.inv(A)
print(Ainv)
#this gives an identity matrix
print(A.dot(Ainv))
print(Ainv.dot(A))

#determinant of matrix
print(np.linalg.det(A))

#dialgonla elements
print(np.diag(A))

a = np.array([3,4])
b = np.array([5,6])

#outer product
c = np.outer(a, b)
print(c)
d = np.inner(a, b)
print(d)
print(np.diag(c).sum())
print(np.trace(c))



X = np.random.randn(100,3)
cov = np.cov(X.T)
print(cov.shape)

#calculating eigen values and eigen vectors
eig = np.linalg.eig(cov)
#first array contains the eigen vectors and the next array contains the correcponding eigen values
print(eig)

#calculating eigen values and eigen vectors
eig = np.linalg.eigh(cov)
#first array contains the eigen vectors and the next array contains the correcponding eigen values
print(eig)

