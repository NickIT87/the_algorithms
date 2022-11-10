def count_numbers(nmb):
    i = 0
    while nmb > 0:
        nmb //= 10
        #print(nmb)
        i+=1
    return i

def check_for_armstrong(nmb):
    i = count_numbers(nmb)
    #print(i)
    armstrong = 0
    while nmb > 0:
        numeric = nmb % 10
        nmb //= 10
        armstrong += pow(numeric, i)
    return armstrong


#num = int(input("Enter number:"))
num = 153
s = check_for_armstrong(num)
     
if s == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")