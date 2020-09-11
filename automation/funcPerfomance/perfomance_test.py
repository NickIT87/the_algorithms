# decorators

from datetime import datetime


def one():
    start = datetime.now()
    l = []
    for i in range(10**4):
        if i % 2 == 0:
            l.append(i)
    print(datetime.now() - start)
    return l

def two():
    start = datetime.now()
    l = [ x for x in range(10**4) if x % 2 == 0]
    print(datetime.now() - start)
    return l

l1 = one()
l2 = two()

#print(l1)
#print(l2)

