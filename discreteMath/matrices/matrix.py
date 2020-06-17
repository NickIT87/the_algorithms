
test_data = [[  0,  1,  2,  3,  4 ],
             [  5,  6,  7,  8,  9 ],
             [ 10, 11, 12, 13, 14 ],
             [ 15, 16, 17, 18, 19 ]]


test_data2 = [[  0,  1,  2,  3,  4,  5,  6 ],
              [  7,  8,  9, 10, 11, 12, 13 ],
              [ 13, 14, 15, 16, 17, 18, 19 ],
              [ 20, 21, 22, 23, 24, 25, 26 ]]


def matrix_position(index, matrix_array=0):
    print("___________________________")
    a, b, c, d, e = range(5)
    # 	    a   b   c   d   e
    W = [[  0,  1,  2,  3,  4 ],  # a
         [  5,  6,  7,  8,  9 ],  # b
         [ 10, 11, 12, 13, 14 ],  # c
         [ 15, 16, 17, 18, 19 ]]  # d
    print(W)
    print("index =", index)
    #print("len(W[a]) =", len(W[a]))
    #print(type(30 / len(W[a])))
    #print(31 / len(W[a]))
    #print(35 / len(W[a]))
    print("___________________________")
    print("***************************")
    G = matrix_array
    print(G)
    print("index: =", index)
    if (G != 0) :
        rows = len(G)
        columns = len(G[0])
        cells = rows * columns
    else:
        rows = 0
        columns = 0
        cells = rows * columns
        print("Ошибка, не передан массив...", G)

    print(cells, rows, columns)
    print(type(G))

    row_position = int(index / columns)
    print("row_position = ", row_position)

    abs_pos = columns - ((columns * (row_position + 1)) - index)
    print("abs_pos: = ", abs_pos)

    print("***************************")


if __name__ == "__main__":
    matrix_position(10, test_data2)
    #matrix_position(13, "asdfasdf")