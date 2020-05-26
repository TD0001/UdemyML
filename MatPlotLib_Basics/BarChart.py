import matplotlib.pyplot as plt

# values = [12, 55, 4, 32, 14]
# color = ['r', 'g', 'b', 'c', 'm']
# plt.bar(range(0,5), values, color= color)
# plt.show()
from pylab import randn

X = randn(500)
Y = randn(500)
print("x=",X)
print("Y=",Y)
plt.scatter(X, Y)
plt.show()