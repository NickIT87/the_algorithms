import numpy as np


for i in np.sctypeDict:
    #print(i)
    pass


a = np.zeros((3,3), dtype='int_')
b = np.full((3,3), 0)
b[0][0] = 1
print(b)


matrix = np.mat('1 2 3; 4 5 6')
print(matrix)
