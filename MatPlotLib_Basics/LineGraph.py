from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.1)
print(x)
plt.plot(x, norm.pdf(x))
# plt.plot(x, "r:")
plt.show()