# 8 class school book task solve 
# for my bro by Nickolazz1

substance = lambda Q, m, dt: Q / (m * dt)
quantityOfHeat = lambda c, m, dt: c * m * dt


def p35_solver():
    """During the combustion of firewood, a brick stove weighing 
	2 tons received 88 megajoules of heat and heated up from 10 to 60 
	degrees Celsius. Determine the specific heat of the brick."""
    m = 2000        # Kg
    t1 = 10         # Celsius
    t2 = 60
    Q = 88000000    # Joule
    c = substance(Q, m, t2 - t1)    
    print(c)    # 880 joule/kg*Celsius
    # DEBUG
    print(Q == quantityOfHeat(c, m, t2 - t1))


def p121_solver(r: float = 0.3, 
                F: complex = complex(32, pow(10, -6)),
                q1: complex = complex(40, pow(10, -9)),
                e: complex = complex(-1.6, pow(10, -19)),
                k: int = 9 * pow(10, 9)): 
    """Two small negatively charged balls are located 
    in the air at a distance of 30 cm from each other. 
    The force of their interaction is 32 μN. Determine 
    the number of excess electrons on the second ball 
    if the charge of the first ball is -40 nC. """
    
    N2 : complex = (F * pow(r, 2)) / (k * abs(q1) * abs(e))
        
    print(type(N2))
    print(N2.real)
    return N2
 

if __name__ == "__main__":
    print(p121_solver())