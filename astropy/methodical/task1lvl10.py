from astropy.constants import G


print(G) # gravitational constant
# Newton's law of gravity: F = G*(M1*M2/r**2)
def powerOfGravity(mass1, mass2, distance):
    F = G.value * mass1 * mass2 / distance**2
    return F

# reduced formula GM**2/4R**2
def altGravityPower(mass, radius):
    F = G.value*mass**2 / (4*radius**2)
    return F


# tasks defenitions M, R, V = M / p
M = 2
R = 2
p = 2.71

M1 = M2 = M
R1 = R2 = R
p1 = p2 = p

Ms = M1s = M2s = 8 * M
r = 2 * R
# V = M / p
# need to solve: F2/F1 = Fabs
F1 = powerOfGravity(M1, M2, r)
F2 = powerOfGravity(M1s, M2s, r)
Fabs = F2 / F1
# generalized solution
F1alt = altGravityPower(M, R)
F2alt = altGravityPower(Ms, R)
Falt = F2alt / F1alt

Rn = 2 * R

# main flow
if __name__ == "__main__":  
    print(f'F1: {F1}')
    print(f'F2: {F2}')
    print(f'Fabs: {Fabs}')

    print(f'F1alt: {F1alt}')
    print(f'F2alt: {F2alt}')
    print(f'Falt: {Falt}')