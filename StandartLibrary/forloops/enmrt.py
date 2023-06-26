def enumerate_example():
    temp = 0
    numbers = [num for num in range(1_000_000)]

    for index, num in enumerate(numbers):
        temp += num
    
    return temp


def zip_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for a_val, b_val in zip(a, b):
        res = a_val + b_val

    return res


print(enumerate_example())