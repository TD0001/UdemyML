import numpy as np
from matplotlib import pyplot as plt

uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))

print('uniformSkewed = ', uniformSkewed)
print('high_outliers = ', high_outliers)
print('low_outliers =', low_outliers)
print(data)

plt.boxplot(data)
plt.show()
# the box represents two inner quartiles where 50% of your data resides
# conversly, another 25% resides on either side
# dotted line whiskers represent the range of date except for outliers
