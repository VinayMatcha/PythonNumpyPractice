from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

print(norm.pdf(0))

print(norm.pdf(0, loc=5, scale=10))

#element wise pdfs
r = np.random.random(10)
print(r)
print(norm.pdf(r))
print(norm.logpdf(r))
print(norm.cdf(r))


#sampling from gaussian
r = np.random.random(10000)
plt.hist(r, bins=20)
r = np.random.randn(10000) * 10 + 5
print(r.shape)
plt.show()
plt.hist(r, bins=100)
plt.show()