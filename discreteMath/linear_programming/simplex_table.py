import pulp

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
a = pulp.LpVariable('a', lowBound=0)
b = pulp.LpVariable('b', lowBound=0)
c = pulp.LpVariable('c', lowBound=0)

# Add the objective function
problem += 13 * a + 18 * b + 22 * c

# Add the constraints
problem += a + b + c == 300
problem += a >= 50
problem += b >= 40
problem += c <= 40

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=True)
status = solver.solve(problem)

# Retrieve the simplex tableau
tableau = []
for name, c in problem.objective.items():
    tableau.append([c, 0] + [v for k, v in problem.constraints.items() if name.name in k])
for v in problem.variables():
    tableau.append([v.value()] + [0]*(len(problem.variables())+len(problem.constraints)-1))
tableau.append([problem.objective.value()] + [0]*(len(problem.variables())+len(problem.constraints)-1))
    
# Print the simplex tableau
for row in tableau:
    print(row)
