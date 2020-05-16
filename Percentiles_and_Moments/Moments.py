import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

print(vals)
print(type(vals))
a = np.mean(vals)
print(a)

b = np.var(vals)
print(b)

c = sp.skew(vals)
print(c)

d = sp.kurtosis(vals)
print(d)