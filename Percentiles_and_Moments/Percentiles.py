import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0,0.5, 1000)
plt.hist(vals, 50)
plt.show()

a = np.percentile(vals, 99)
print(a)
b = np.percentile(vals, 50)
print(b)