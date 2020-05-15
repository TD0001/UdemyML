#aka Gaussian

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
print('x = ',x)
plt.show()
# "mu" is the desired mean, "sigma" is the standard deviation:
mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
print(values)
values.sort()
print(values)
print(np.median(values))
# plt.show()