import numpy as np

a = np.array([1,2,3])
b = np.array([3,4,5])

print(a*b)

print(np.dot(a, b))

print(np.dot(a.T, b))

print((a*b).sum())
print(np.sum(a*b))
print(a.dot(b))

#a magnitude

amag = np.linalg.norm(a)
bmag = np.linalg.norm(b)

cosangle = a.dot(b)/(amag*bmag)

print(cosangle)

angle = np.arccos(cosangle)
print("angle between a and b is ", angle, " radians")