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




# Covariance is sensitive to the units used in the variables,
# which makes it difficult to interpret.
# Correlation normalizes everything by their standard deviations,
# giving you an easier to understand value that
# ranges from -1 (for a perfect inverse correlation) to 1 (for a perfect positive correlation):

# ------------------------------------------------------------------------


# We can force a perfect correlation by fabricating a totally linear relationship
# (again, it's not exactly -1 just due to precision errors,
# but it's close enough to tell us there's a really good correlation here):
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - pageSpeeds * 3
print("pageSpeeds = ", pageSpeeds)
print("purchaseAmount = ", purchaseAmount)


print("--------------------------------------")
print("pageSpeeds = ", pageSpeeds)
print("purchaseAmount = ", purchaseAmount)


print("--------------------------------------")

correla = correlation(pageSpeeds, purchaseAmount)
print(correla)

print("----------------------------")

co = covariance (pageSpeeds, purchaseAmount)
print("covariance = ",co)

conumpy = np.cov(pageSpeeds, purchaseAmount)
print("covariance by numpy = ", conumpy)

print("----------------------------------------------")
num_py = np.corrcoef(pageSpeeds, purchaseAmount)
print(num_py)


scatter(pageSpeeds, purchaseAmount)
plt.xlabel('pageSpeeds')
plt.ylabel('purchaseAmount')
plt.savefig('co.png')
plt.show()