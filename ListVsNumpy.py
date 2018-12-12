import numpy as np

li = [1,2,3]
A = np.array([1,2,3])

for i in li:
    print(i)

for i in A:
    print(i)

li.append(4)
li.append(5)

print(li)

#in order for adding each element to it in list we have to loop whihc is not necessary in numpy

l2 = []
for i in li:
    l2.append(i+i)
print(l2)

#matrix addition
print(A+A)
print(2*A)

#multiplication doubles the list
print(2*l2)

l3 = []
for i in l2:
    l3.append(i**2)

print(l3)
print(A**2)

print(np.sqrt(A))
print(np.exp(A))
print(np.log(A))