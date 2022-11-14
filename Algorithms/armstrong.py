def count_numbers(nmb: int) -> int:
    i: int = 0       # кількість цифр у числі
    while nmb > 0:
        nmb //= 10
        #print(nmb)
        i+=1
    return i    # повертає необхідний показник степеню 

def check_for_armstrong(nmb: int) -> bool:
    num: int = nmb          # актуальне число
    ansver = 0           
    i = count_numbers(nmb)  # показник степеню
    
    while nmb > 0:  
        numeric = nmb % 10
        nmb //= 10
        ansver += numeric ** i
    
    return ansver == num


def isArmstrong(number: int) -> bool:
    return sum((int(digit) ** len(str(number)) for digit in str(number))) == number


#num = int(input("Enter number:"))
num = 153
s = check_for_armstrong(num)
#s = isArmstrong(num)

if s:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")