from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9,9,1)

axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 0.5])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid() #add a grid
plt.xlabel('Greebles')
plt.ylabel('Probability')

plt.plot(x, norm.pdf(x), 'g-.')
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.legend(['Sneetches', 'Gacks'], loc = 4)
plt.show()