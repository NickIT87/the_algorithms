import numpy as np
import matplotlib.pyplot as plt

# Define the objective function and constraints
def objective_function(x):
    return 2 * x + 6

def constraint1(x):
    return (25 - 3 * x) / 4

def constraint2(x):
    return 10 - 2 * x

# Create a grid of x and y values
x = np.linspace(0, 10, 100)
y1 = constraint1(x)
y2 = constraint2(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, objective_function(x), label='Objective Function')
ax.plot(x, y1, label='Constraint 1')
ax.plot(x, y2, label='Constraint 2')
ax.axvline(0, color='black')
ax.axhline(0, color='black')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Find the intersection points of the constraints
A = np.array([[3, 4], [2, 1]])
b = np.array([25, 10])
intersection = np.linalg.solve(A, b)

# Plot the intersection points
ax.plot(intersection[0], intersection[1], 'ro')
ax.annotate('Optimal Point', xy=intersection, xytext=(intersection[0] - 1, intersection[1] + 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Print the optimal solution
print('Optimal value:', objective_function(intersection[0]))
print('Optimal solution:', intersection)

plt.show()

#In this example, we define the objective function 2x + y and two constraints: 
# 3x + 4y <= 25 and 2x + y <= 10. We create a grid of x and y values, 
# plot the objective function and constraints, and find the intersection 
# points of the constraints. We then plot the intersection points and annotate 
# the optimal point, which is the intersection of the constraints that maximizes 
# the objective function. Finally, we print the optimal value and solution.