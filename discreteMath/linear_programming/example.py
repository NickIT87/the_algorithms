import pulp

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

# Add the objective function
problem += 2 * x + y

# Add the constraints
problem += 3 * x + 4 * y <= 25
problem += 2 * x + y <= 10

# Solve the problem
status = problem.solve()

# Print the status and optimal value
print("Status:", pulp.LpStatus[status])
print("Optimal Value:", pulp.value(problem.objective))

# Print the optimal solution
for var in problem.variables():
    print(var.name, "=", var.varValue)
