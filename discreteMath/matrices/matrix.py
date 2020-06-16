def matrix(index):
    a, b, c, d, e, f, g = range(7)
    # 	   a   b   c   d   e   f
    W = [[ 0,  1,  2,  3,  4,  5 ],  # a
         [ 6,  7,  8,  9, 10, 11 ],  # b
         [12, 13, 14, 15, 16, 17 ],  # c
         [18, 19, 20, 21, 22, 23 ],  # d
         [24, 25, 26, 27, 28, 29 ],  # e
         [30, 31, 32, 33, 34, 35 ],  # f
         [36, 37, 38, 39, 40, 41 ]]  # g

    print("index =", index)
    print("len(W[a]) =", len(W[a]))

    print(type(30 / len(W[a])))
    print(31 / len(W[a]))
    print(35 / len(W[a]))



if __name__ == "__main__":
    matrix(25)