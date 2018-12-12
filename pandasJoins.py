import pandas as pd

#takes tables 1 and 2 and jooins boith of them

t1 = pd.read_csv('table1.csv')
t2 = pd.read_csv('table2.csv')
print(t1)
print(t2)

m = pd.merge(t1, t2, on="user_id")
print(m)
m = t1.merge(t2, on="user_id")
print(m)