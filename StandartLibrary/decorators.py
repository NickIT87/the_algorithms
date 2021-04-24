# decoratos
from datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper


@timeit
def one():
    l = []
    for i in range(10**4):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two():
    l = [x for x in range(10**4) if x % 2 == 0]
    return l


l1 = one()
l2 = two()
