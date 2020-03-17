# load data from files
import matplotlib.pyplot as plt

# Part 1
'''
import csv

x = []
y = []

with open('examples.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))


plt.plot(x,y, label='loaded from file!')
'''
# Part 2

import numpy as np

x, y = np.loadtxt('examples.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='loaded from file!')


plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interesting Graph\ncheck it out")
plt.legend()
plt.show()