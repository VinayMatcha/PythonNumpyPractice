import numpy as np
from datetime import datetime


a = np.random.random(100)
b = np.random.random(100)

T =100000
start = datetime.now()
for t in range(T):
    result = 0
    for i,j in zip(a,b):
        result += i*j
end = datetime.now()
print(result)
print("time ttaken is ", end-start)

start = datetime.now()
for t in range(T):
    result1 = np.sum(a.dot(b))
end =  datetime.now()

print(result1)
print("time ttaken is ", end-start)