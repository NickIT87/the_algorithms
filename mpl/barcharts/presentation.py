# harmonic vibrations
import matplotlib.pyplot as plt
import numpy as np
import math


# defenitions
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
c = np.cos(2 * t * math.pi)

# plot settings
fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t, c)

# graph settings
ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()