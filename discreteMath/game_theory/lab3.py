import random
import numpy as np
import matplotlib.pyplot as plt


def get_sample(m, n, C1, C2):
    sample = np.array([ [random.randint(0, 10) for i in range(n)] for j in range(m) ])
    if C1 not in sample:
        t1 = True
        while t1:
            dice_row = random.randint(0, m-1)
            dice_col = random.randint(0, n-1)
            if sample[dice_row][dice_col] != C2:
                sample[dice_row][dice_col] = C1
                t1 = False        
    if C2 not in sample:
        t2 = True
        while t2:
            dice_row = random.randint(0, m-1)
            dice_col = random.randint(0, n-1)
            if sample[dice_row][dice_col] != C1:
                sample[dice_row][dice_col] = C2
                t2 = False
    return sample


def saddle_point(sample):
    for i in range(0, sample.shape[0]):
        for j in range(0, sample.shape[1]):
            row_point = min(sample[i, :] )
            column_point = max(sample[:, j] )
            if row_point == column_point:
                return True
    return False


def generate_game_matrix(m, n, C1, C2, s_point=True):
    g_matrix = np.array([])
    if s_point:
        trig1 = True
        while trig1:
            s = get_sample(m, n, C1, C2)
            if saddle_point(s):
                g_matrix = s
                trig1 = False
    else:
        trig2 = True
        while trig2:
            s = get_sample(m, n, C1, C2)
            if not saddle_point(s):
                g_matrix = s
                trig2 = False
    return g_matrix
    

def find_minimal_price_maximin(g_matrix):
    values = []
    for i in g_matrix:
        values.append(min(i))
    return max(values)


def find_maximal_price_minimax(g_matrix):
    values = []
    for i in range(g_matrix.shape[1]):
        values.append(max(g_matrix[:, i]))
    return min(values)


# task 3
n = 3
m = 2
C1 = 0
C2 = 7

g_m = generate_game_matrix(m, n, C1, C2, s_point=False)
min_price = find_minimal_price_maximin(g_m)
max_price = find_maximal_price_minimax(g_m)

print(g_m)
print("min: ", min_price)
print("max: ", max_price)

line1 = g_m[:, 0]
line2 = g_m[:, 1]
line3 = g_m[:, 2]


plt.plot(line1, color='red')
plt.plot(line2, color='green')
plt.plot(line3, color='blue')
plt.show()