#the algorithms

def quantityOfHeat(c, m, dt):

    Q = c * m * dt

    return Q


if __name__ == "__main__":
    print(quantityOfHeat(880, 2000, 50))