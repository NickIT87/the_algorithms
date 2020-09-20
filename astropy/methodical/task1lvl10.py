from astropy.constants import G
print(G) # gravitational constant

# tasks defenitions
M = 2
R = 2
p = 2
M1 = M2 = M
R1 = R2 = R
M1s = M2s = 8 * M
p1 = p2 = p
r = 2 * R
# need to solve: F2/F1 = ?

# Newton's law of gravity: F = G*(M1*M2/r**2)
def powerOfGravity(mass1, mass2, distance):
    F = G.value * (mass1 * mass2 / distance**2)
    return F

F1 = powerOfGravity(M1, M2, r)

F2 = powerOfGravity(M1s, M2s, r)

print(F1)
print(F2)
