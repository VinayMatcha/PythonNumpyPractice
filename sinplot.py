import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("values")
plt.ylabel("sin values")
plt.title("Sin function plotting")
plt.show()
plt.savefig("sin.png")