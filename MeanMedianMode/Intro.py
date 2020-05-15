import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(27000,15000,10000)
# np.mean(incomes)
print(incomes)

print(np.mean(incomes))
plt.hist(incomes,50)
plt.show()

print("----------")
ages = np.random.randint(18, high=90,size=501)
print(ages)

import scipy.stats as stat
statistic = stat.mode(ages)
print(statistic)
print(np.median(ages))
