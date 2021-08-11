def count_numbers():
    f = open('number.txt', 'r')
    lines = f.readlines()
    l = [line.rstrip() for line in lines]
    ansv = 0
    for i in l:
        if (i.find('#', 0) == 0):
            continue
        try:
            ansv += float(i)
        except:
            continue

    return ansv


if __name__ == "__main__":
    print(count_numbers())