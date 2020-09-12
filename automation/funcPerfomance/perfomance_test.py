# decorators

from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def one(n):
    l = []
    for i in range(n**2):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def two(n):
    l = [ x for x in range(n**2) if x % 2 == 0]
    return l

l1 = one(10000)
l2 = two(10000)

#print(l1)
#print(l2)

