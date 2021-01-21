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


if __name__ == "__main__":
    p35_solver()