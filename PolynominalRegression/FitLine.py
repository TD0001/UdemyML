import matplotlib.pyplot as plt
from pylab import *
import numpy as np

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

# numpy has a handy polyfit function we can use,
# to let us construct an nth-degree polynomial model of
# our data that minimizes squared error.
# Let's try it with a 4th degree polynomial:

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

print("-------------------------------------------------------------------------------------")
p4 = np.poly1d(np.polyfit(x, y, 4))

print("x= ", x)
print("-------------------------------------------------------------------------------------")
print("y= ", y)
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")
p4 = np.poly1d(np.polyfit(x, y, 4))

print("===================================================================================")
print("p4 = ",p4)

# We'll visualize our original scatter plot,
# together with a plot of our predicted values using
# the polynomial for page speed times ranging from 0-7 seconds:
xp = np.linspace(0, 7, 100)
print("-----------------------------------------------------------------------------------")
print("xp =", xp)
print("-------------------------------------------------------------------------------------")
print("p4(xp)", p4(xp) )
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

from sklearn.metrics import r2_score

r2 = r2_score(y, p4(x))
print("-------------------------------------------------------------------------------------")
print("r2(r-squared error) =", r2)

























