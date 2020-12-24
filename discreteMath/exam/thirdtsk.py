
data = [[1, 3, 5, 7],
        [4, 2, 0, 4]]

def totalOddElem(data_array):
    ansv = 0
 
    for i in range(0, len(data_array)):
        for j in range(0, len(data_array[i])):
            if j % 2 != 0:
                print(data_array[i][j])
                ansv = ansv + data_array[i][j]

    return ansv

debug_data = [[1, 2, 3, 4],
              [1, 2, 3, 4]]

if __name__ == "__main__":
    print(totalOddElem(data))