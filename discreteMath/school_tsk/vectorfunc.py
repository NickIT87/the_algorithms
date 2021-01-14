import numpy as np

alpha = (12, 32, 34)
beta = (34, 67, 89)

def vectorSum(X, Y):
    return X + Y

def add_vectors(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


y = tuple(add_vectors(alpha, beta))

print(y)


vector1 = np.array([235, 345, 324])
vector2 = np.array([768, 354, 678])

print(vector1 + vector2)