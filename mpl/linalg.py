import numpy as np

a = np.array([[2, -1], [-1, 2]])
b = np.array([0,3])
print(np.linalg.solve(a,b))

c = np.array([[2, -1, 0],[-1, 2, -1],[0, -3, 4]])
d = np.array([0, -1, 4])
print(np.linalg.solve(c,d))

e = np.array([[2,-1,0],[-1,2,3],[0,-1,4]])
f = np.array([1,1,-3])
print(np.linalg.solve(e,f))