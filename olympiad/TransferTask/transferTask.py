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

a, b, c, d, e, f = range(6)

N = [
	[b,e], # a
	[a,c,e], # b
	[b,d], # c
	[c,e,f], # d
	[a,b,d], # e
	[d], # f
]

#     a b c d e f
G = [[0,1,0,0,1,0], # a
	 [1,0,1,0,1,0], # b
	 [0,1,0,1,0,0], # c
	 [0,0,1,0,1,1], # d
	 [1,1,0,1,0,0], # e
	 [0,0,0,1,0,0]] # f
