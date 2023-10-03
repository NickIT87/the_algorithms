from sympy import Eq, solve, symbols

# Define the variable
x = symbols('x')

# Define the equation
#equation = Eq(2**x - 5*x+1, 0)
equation = Eq(2**x, 5*x + 1)

# Solve the equation
solutions = solve(equation, x)

# Print the solutions
print(solutions)

