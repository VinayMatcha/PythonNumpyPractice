import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = pd.read_csv("data_1d.csv", header=None).values
x = A[:,0]
y = A[:,1]

plt.scatter(x, y)
plt.show()
plt.savefig("scatterplt")