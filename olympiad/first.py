original_data = [44, 6, 32, 3, 5, 44, 21, 23, 32, 34, 0, 44, 88, 23, 88, 23, 43, 1, 2, 3, 4, 5, 6, -5]
test_data1 = [44, 44, 44, 44]
test_data2 = []

def solution(dat):
    # проверка на не пустой массив
    if len(dat) == 0:
        raise Exception('error, no numbers!')
    # начальные преобразования
    dat.sort()
    dat.reverse()
    max = dat[0]
    counter = 0
    # основной цикл программы
    for i in range(0, len(dat)):
        if dat[i] == max:
            counter+=1
    return counter

if __name__ == '__main__':
    print(solution(original_data))