original_data = 342345

def solution(dat):
   answer = []
   i = 2
   while i * i <= dat:
       if dat % i == 0:
           answer.append(i)
           dat //= i
       else:
           i += 1
   if dat > 1:
       answer.append(dat)
   return answer


if __name__ == "__main__":
    print(solution(original_data))

