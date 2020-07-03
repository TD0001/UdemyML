from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3
print("pageSpeeds = ", pageSpeeds)
print("===========================================================================================")
print("purchase amount =", purchaseAmount)

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

print("r_value = ", r_value)
print("p_value = ", p_value)
print("slope = ", slope)
print("intercept = ", intercept)
print("std_err = ", std_err)

def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()