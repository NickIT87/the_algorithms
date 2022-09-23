# https://youtu.be/fW_OS3LGB9Q
# https://www.youtube.com/watch?v=fW_OS3LGB9Q&t=745s


def recur_factorial(n):
    if n <= 1:
        return 1
    else:
        return n*recur_factorial(n-1)

a = []

for i in range(10):
    a.append(recur_factorial(i))

print(a)


def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact