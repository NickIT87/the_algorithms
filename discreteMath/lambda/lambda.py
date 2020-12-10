# 8 class school book task solve 
# for my bro by Nickolazz1

substance = lambda Q, m, dt: Q / (m * dt)
quantityOfHeat = lambda c, m, dt: c * m * dt

def main():
    m = 2000
    t1 = 10
    t2 = 60
    Q = 88000000


    c = substance(Q, m, t2 - t1)
    print(c)
    # DEBUG
    #print(Q == quantityOfHeat(c, m, t2 - t1))


if __name__ == "__main__":
    main()