import numpy as np
import pandas as pd

X = []
for line in open("data_2d.csv"):
    row = line.split(',')
    #converting into floats from strings
    sample = list(map(float, row))
    X.append(sample)
print(X)
X = np.array(X)
print(X.shape)


#Using Pandas to read csv files
X = pd.read_csv("data_2d.csv", header = None)
print(type(X))
print(X.info())
#to know the rows
print(X.head())
print(X.head(3))