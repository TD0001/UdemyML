from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9,9,1)
print(x)
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1, 0.5)) #mean around 1.0 and standard
 #deviation of 0.5

plt.savefig('MyPlot.png', format = 'png')
plt.show()