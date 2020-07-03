import matplotlib.pyplot as plt
import numpy as np
from pylab import *

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


# scatter(pageSpeeds, purchaseAmount)
print("pageSpeeds = ", pageSpeeds)
print("purchaseAmount = ", purchaseAmount)

# Now we'll split the data in two -
# 80% of it will be used for "training" our model,
# and the other 20% for testing it.
# This way we can avoid overfitting.
print("\n----------------------------------------------------------------------------")
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

scatter(testX, testY)

print("testX = ", testX)
print("testY = ", testY)

plt.show()