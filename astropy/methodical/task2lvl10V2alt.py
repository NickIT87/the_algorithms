"""
A meteorite weighing 100 kg, falls into the sea at a speed of 50
km / s. Determine the mass of water converted to steam.
The water temperature is 20 degrees Celsius. Specific heat of
water: 4.2 * 10 ** 3 J / kg * K. Specific heat of transformation
of water: 2.3 * 10 ** 6 J / kg.
"""
# Task defenitions, meteor data:
m = 100                 # kg
v = 50                  # km/s
t1 = 20                 # celsius degree
t2 = 100
c = 4200                # J / (kg * celsius)
L = 2.3 * pow(10, 6)    # J / kg
mv = 0                  # ? need to solve ...
# solution
Ek = (m*v**2) / 2

if __name__ == "__main__":
    print(Ek)
