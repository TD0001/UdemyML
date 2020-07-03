import matplotlib.pyplot as np
import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

scatter(pageSpeeds, purchaseAmount)


print(pageSpeeds)
print('---------------------------------------LMAO---------------------')
print(de_mean([1,2,3,4,5]))

co = covariance (pageSpeeds, purchaseAmount)
print(co)
print("--------------------------")
co_by_numpy = np.cov(pageSpeeds, purchaseAmount)
print("covariance by numpy: ", co_by_numpy)
plt.show()