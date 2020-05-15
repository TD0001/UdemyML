from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n, p = 10, 0.5
x = np.arange(0,10, 0.001)
plt.plot(x, binom.pmf(x, n, p))
plt.show()
# The binomial distribution consists of the probabilities of
# each of the possible numbers of
# successes on N trials for independent events
# that each have
# a probability of π (the Greek letter pi) of occurring.