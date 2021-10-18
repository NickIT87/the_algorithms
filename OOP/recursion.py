# test example recursion
def rec(x):
    if x < 4:
        print(x)
        rec(x+1)
        print(x)

# recursion factorial
def factorial(x):
    if x == 1 or x==0:
        return 1
    return factorial(x-1)*x

# cycle factorial, no recursion
def factorial_norec(x: int):
    fact=1 
    for i in range(2,x+1): 
        fact *= i
    return fact

# Fibonacci recursion
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

# palindrom recursion
def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

#rec(1)
#print(factorial(5))
#print(factorial_norec(9))
#print(fibonacci(5))
print(palindrom('шалаш'))