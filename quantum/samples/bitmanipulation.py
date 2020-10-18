# binary convertations
bin_a = "01010101"

#print(int(bin_a, 2))

bin_b = bin(123)

#print(type(bin_b))
#print(int(bin_b, 2))

#print(bin(9)) 
#   6:    0110
#   9:    1001
#   15:   1111
bitstr1 = "11111111"
bitstr2 = "01101001"
#print(int(bitstr1, 2), int(bitstr2, 2))

print( "11111111" and bitstr2 )    # solution for find some bit value

#print(int(bitstr1, 2) and int(bitstr2, 2))

print(int(bin(15) and bin(6), 2))