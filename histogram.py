import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = pd.read_csv("data_1d.csv", header=None).values
x = A[:,0]
y = A[:,1]

plt.hist(x)
plt.show()
plt.savefig("histogram")

x = np.random.random(10000)
plt.hist(x, bins=20)
plt.show()
plt.savefig("Random function with 10000 pints")

x = np.random.randn(10000)
plt.hist(x, bins=20)
plt.show()
plt.savefig("gaussiam functiopn")