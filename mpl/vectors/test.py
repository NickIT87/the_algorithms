import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from random import randint


x=np.array([randint(0,100) for x in range(10)])
y=np.array([0 for x in range(10)])
z=np.array([0 for x in range(10)])


fig=plt.figure()
axes = plt.axes(projection='3d')

axes.set_xlabel("x", color='black')
axes.set_ylabel("y", color='black')
axes.set_zlabel("z", color='black')

axes.tick_params(axis='x', colors='r')
axes.tick_params(axis='y', colors='g')
axes.tick_params(axis='z', colors='b')

axes.set_xlim([-100,100])
axes.set_ylim([-100,100])
axes.set_zlim([-100,100])

axes.set_title('3D line plot geeks for geeks', color='Black')

line=axes.plot3D(x,y,z,'red')


red_patch = mpatches.Patch(color='red', label='The red data')
axes.legend(handles=[red_patch])

plt.show()