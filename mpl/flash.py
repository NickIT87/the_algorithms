import matplotlib.pyplot as plt
from numpy import linspace, pi, sin, cos


x = linspace(0, 2*pi, 100)
y = sin(x)
z = cos(x)

plt.plot(x, y, 'ro-')
plt.plot(x, z, 'bo-')
plt.show()
