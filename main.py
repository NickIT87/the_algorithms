#the algorithms

def quantityOfHeat(c, m, dt):

    Q = c * m * dt

    return Q


a = [1, 2, 3]



def test():
    t = True
    c = 0
    while t:
        print("While ... ")
        t = False   
        for i in range(10):
            print("For ...", i)
            c += i
            if i > 5:
                break
        if c < 5:
            t = True
    print(c)



if __name__ == "__main__":
    #print(quantityOfHeat(880, 2000, 50))
    test()