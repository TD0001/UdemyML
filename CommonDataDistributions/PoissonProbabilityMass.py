from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

#   My website gets on average 500 visits per day
mu = 500
x = np.arange(400,600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()
# to see the probability of some other values on a specific day