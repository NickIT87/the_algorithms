def calPoints(ops) -> int:
    result = None
    record = []

    for i in ops:
        
        print(i)
        print(record)
        
        if i.lstrip("-").isdigit():
            record.append(int(i))
        elif i == "C":
            record.pop()
        elif i == "D":
            record.append(2 * record[-1])
        elif i == "+" and len(record) > 1:
            record.append(record[-2] + record[-1])

    print(record)
    result = sum(record)

    return result


if __name__ == '__main__':
    line = input()
    ops = line.strip().split()
    print(ops)

    print(calPoints(ops))



# 5 -2 4 C D 9 + + 
# 71  27