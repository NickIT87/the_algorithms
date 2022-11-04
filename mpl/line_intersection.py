# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 1000)
# f = np.arange(0, 1000)
# g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000
# z = np.arange(100, 1100)

# plt.plot(x, f, '-')
# plt.plot(x, g, '-')
# plt.plot(x, z)

# idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
# plt.plot(x[idx], f[idx], 'ro')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from shapely.geometry import LineString

# x = np.arange(0, 1000)
# f = np.arange(0, 1000)
# g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000

# plt.plot(x, f)
# plt.plot(x, g)

# first_line = LineString(np.column_stack((x, f)))
# second_line = LineString(np.column_stack((x, g)))
# intersection = first_line.intersection(second_line)

# print(intersection[0])

# plt.scatter(intersection[2], intersection[2], label='skitscat', color='k', marker='*', s=200)

# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

g_m = np.array([ 
    [20, 0, 37],
    [17, 51, 7]
])

line1 = g_m[:, 0]
line2 = g_m[:, 1]
line3 = g_m[:, 2]

plt.plot(line1, color='red')
plt.plot(line2, color='green')
plt.plot(line3, color='blue')

print(line1)

first_line = LineString(
    [
        [0, line1[0]], 
        [1, line1[1]]
    ]
)
second_line = LineString([[0, line2[0]], [1, line2[1]]])
intersection = first_line.intersection(second_line)

print(intersection.coords[0])

plt.scatter(intersection.coords[0][0], intersection.coords[0][1], label='skitscat', color='k', marker='*', s=200)

plt.show()