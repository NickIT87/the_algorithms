# binary convertations
bin_a = "01010101"

print(int(bin_a, 2))

bin_b = bin(123)

print(type(bin_b))
print(int(bin_b, 2))

# xor operation
x = True
y = False

print((x ^ y) ^ y)

# swap algorithm
a = 2
b = 8

a ^= b
b ^= a
a ^= b

print(a, b)

# ternary conjunction

def rgb(r, g, b):
    return r ^ g ^ b

print(rgb(1,0,1))

# fibonacci

def fib(n):
    return 1 if (n <= 2) else fib(n-1)+fib(n-2)

print(fib(20))