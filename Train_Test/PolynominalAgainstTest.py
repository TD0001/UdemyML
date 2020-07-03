import matplotlib.pyplot as plt
import numpy as np
from pylab import *

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


# scatter(pageSpeeds, purchaseAmount)
# print("pageSpeeds = ", pageSpeeds)
# print("purchaseAmount = ", purchaseAmount)

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

x = np.array(trainX)
y = np.array(trainY)

testx = np.array(testX)
testy = np.array(testY)

p4 = np.poly1d(np.polyfit(x, y, 8))
xp = np.linspace(0, 7, 100)

axes = plt.axes()
axes.set_xlim([0,7])

axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
plt.show()

from sklearn.metrics import r2_score

r2 = r2_score(testy, p4(testx))

print(r2)
print(" the r-squared score on the test data is kind of horrible! This tells us that our model isn't all that great.")
r2 = r2_score(np.array(trainY), p4(np.array(trainX)))
print("-------------------------------------------")
print("r-squared of train", r2)