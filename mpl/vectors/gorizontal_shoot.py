import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g

# condition
V0 = 253
t = 8
alpha = 45

#sind = lambda degrees: np.sin(np.deg2rad(degrees))
#cosd = lambda degrees: np.cos(np.deg2rad(degrees))
#print(sind(90)) # Output 1.0


x=np.array([V0*x*np.cos(np.deg2rad(alpha)) for x in range(t)])
y=np.array([0 for x in range(t)])
z=np.array([V0*x*np.sin(np.deg2rad(alpha)) - (0.5*g*x)**2 for x in range(t)])


fig=plt.figure()
axes = plt.axes(projection='3d')

axes.set_xlabel("x", color='black')
axes.set_ylabel("y", color='black')
axes.set_zlabel("z", color='black')

axes.tick_params(axis='x', colors='r')
axes.tick_params(axis='y', colors='g')
axes.tick_params(axis='z', colors='b')

axes.set_xlim([-10,1500])
axes.set_ylim([-10,10])
axes.set_zlim([-10,700])

axes.set_title('3D line plot geeks for geeks', color='Black')

line=axes.plot3D(x,y,z,'red')


red_patch = mpatches.Patch(color='red', label='The red data')
axes.legend(handles=[red_patch])

print(len(x))
print(len(z))
plt.show()