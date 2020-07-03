import matplotlib.pyplot as plt
from pylab import *
import numpy as np

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
plt.show()

# numpy has a handy polyfit function we can use,
# to let us construct an nth-degree polynomial model of
# our data that minimizes squared error.
# Let's try it with a 4th degree polynomial:

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))

print("x= ", x)
print("y= ", y)

p4 = np.poly1d(np.polyfit(x, y, 4))

print("===================================================================================")
print(p4)