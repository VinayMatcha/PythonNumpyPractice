import pandas as pd

#Using Pandas to read csv files
X = pd.read_csv("data_2d.csv", header = None)
print(type(X))
print(X.info())
#to know the rows
print(X.head())
print(X.head(3))

#converting to matrix
m = X.values
print(type(m))
#gives column values of all sets
print(type(X[0]))

#to get rows
print(X.iloc[0])
print(X.loc[3])

#to get 0 and 2nd columns

print(X[[0,2]])
print(X[X[0]<5])