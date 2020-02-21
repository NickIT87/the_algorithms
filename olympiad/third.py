original_data = 345432
test_data = 454

def solution(dat):
    answer = []

    while dat != 0:
        answer.append(dat % 7)
        dat //= 7

    answer.reverse()
    answ = int(''.join([str(i) for i in answer]))

    if answ % 2 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solution(original_data)