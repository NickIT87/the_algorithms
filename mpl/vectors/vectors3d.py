import numpy as np
import matplotlib.pyplot as plt

u = np.array([1, 2, 3])   # vector u
v = np.array([5, 6, 2])   # vector v:
  
fig = plt.figure()
ax = plt.axes(projection = "3d")

start = [0,0,0]
ax.quiver(start[0],start[1],start[2],u[0],u[1],u[2],color='red')            # u
ax.quiver(start[0],start[1],start[2],v[0],v[1],v[2])                        # v
sum_vector = u+v
ax.quiver(start[0], start[1], start[2], sum_vector[0], sum_vector[1], sum_vector[2],  color="green")

ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim([-10,10])
plt.show()