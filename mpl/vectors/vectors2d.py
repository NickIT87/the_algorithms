import numpy as np                  # двумерн. массив
import matplotlib.pyplot as plt     # graph


def draw(x, y): 
    xPlusy = (abs(x[0]+y[0]),abs(x[1]+y[1]))
    array = np.array([[0, 0, x[0], x[1]], 
                      [x[0], x[1], y[0], y[1]], 
                      [0, 0, xPlusy[0], xPlusy[1]]])
    print(array)
    X, Y, U, V = zip(*array)
    print("X =",X)
    print("Y =",Y)
    print("U =",U)
    print("V =",V)
    plt.figure()
    plt.ylabel('Y-axis')
    plt.xlabel('X-axis')
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy',color=['r','b','g'],scale=1)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    plt.draw()
    plt.show()

draw([4,2],[2,4])