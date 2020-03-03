# graphs representation in progress

file = open('data.txt', 'r')
temp = file.read()
data = []

for c in temp:
	try:
		data.append(int(c))
	except:
		pass

print(data)
print("     ")
# [3, 4, 0, 1, 1, 2, 4, 0, 1, 4, 4, 3, 3, 5, 2, 3]

##     0 1 2 3 4 5
##     a b c d e f
##    [0 1 0 0 1 0] a 0
##    [1 0 1 0 1 0] b 1
##    [0 1 0 1 0 0] c 2
##    [0 0 1 0 1 1] d 3
##    [1 1 0 1 0 0] e 4
##    [0 0 0 1 0 0] f 5


#     0 1 2 3 4 5
#     a b c d e f
T = [[0,0,0,0,0,0], # a 0
	 [0,0,0,0,0,0], # b 1
	 [0,0,0,0,0,0], # c 2
	 [0,0,0,0,0,0], # d 3
	 [0,0,0,0,0,0], # e 4
	 [0,0,0,0,0,0]] # f 5

T[0][1] = 1
T[1][0] = 1

T[1][2] = 1
T[2][1] = 1

T[4][0] = 1
T[0][4] = 1

T[1][4] = 1
T[4][1] = 1

T[4][3] = 1
T[3][4] = 1

T[3][5] = 1
T[5][3] = 1

T[2][3] = 1
T[3][2] = 1

for i in T:
	print(i)



