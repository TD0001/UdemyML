import matplotlib.pyplot as np
import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  #In real life you'd check for divide by zero here



pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
print("pageSpeeds = ", pageSpeeds)
print("purchaseAmount = ", purchaseAmount)


print("--------------------------------------")

# Covariance is sensitive to the units used in the variables,
# which makes it difficult to interpret.
# Correlation normalizes everything by their standard deviations,
# giving you an easier to understand value that
# ranges from -1 (for a perfect inverse correlation) to 1 (for a perfect positive correlation):

correla = correlation(pageSpeeds, purchaseAmount)
print(correla)

print("----------------------------")

co = covariance (pageSpeeds, purchaseAmount)
print(co)

print("----------------------------------------------")
num_py = np.corrcoef(pageSpeeds, purchaseAmount)
print(num_py)

scatter(pageSpeeds, purchaseAmount)
plt.show()