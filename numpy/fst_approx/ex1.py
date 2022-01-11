import numpy as np

# empty
a = np.array([])
print(a.dtype)

b = np.array([1, "2", True])
print(b)

c = np.array([1,2,3,4,5,6,7,8,9])
c = c.reshape(3, 3)
print(c)
c = c.reshape(len(c)*len(c[0]))
print(c)
