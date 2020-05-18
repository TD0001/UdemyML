import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0,20.0,10000) #10000 data points
# incomes = np.array([1,4,5,4,8])
plt.hist(incomes, 50)

plt.show()
print(incomes)
print("Standard Deviation: ", incomes.std())
print("Variance: ", incomes.var())
