# graphs computations in progress...

def loadDataString():
	file = open('data.txt', 'r')
	data = []
	for line in file:
		data.append(line)
	return data

def loadDataArray():
	file = open('data.txt', 'r')
	temp = file.read()
	data = [] # [3, 4, 0, 1, 1, 2, 4, 0, 1, 4, 4, 3, 3, 5, 2, 3]
	for c in temp:
		try:
			data.append(int(c))
		except:
			pass
	return data

def makeGraph(data, datastr):
	rnum = max(data) + 1
	T =	[[ 0 for j in range(rnum)] for i in range(rnum)]
	temp = []

	for i in range(2, len(datastr)):
		t = datastr[i]
		for c in t:
			try:
				temp.append(int(c))
			except:
				pass
		T[temp[0]][temp[1]] = 1
		T[temp[1]][temp[0]] = 1
		temp = []

	return T
	##     0 1 2 3 4 5
	##     a b c d e f
	##    [0 1 0 0 1 0] a 0
	##    [1 0 1 0 1 0] b 1
	##    [0 1 0 1 0 0] c 2
	##    [0 0 1 0 1 1] d 3
	##    [1 1 0 1 0 0] e 4
	##    [0 0 0 1 0 0] f 5

def computations(G, start, finish):
	#for i in G:
	#	print(i)
	#print(start, finish)
	# print(G[0][1]) 		# проверка ребра
	# print(sum(G[0])) 	# кол-во смежных вершин

	stack = []
	queue = []
	visited = []
	V_counter = 0
	for i in range(0,len(G)):
		visited.append(False) # DO REFACTOR
	#stack.append(start)
	queue.append(start)
	visited[start] = True
	print(visited)
	r = [1]
	cycle_counter = 0
	while len(r) != 0:
		cycle_counter += 1
		node = queue.pop()
		if(node == finish):
			print(node)
		print("node", node)
		V_counter = sum(G[node])
		print("Vertecies_counter: ",  V_counter)
		for i in range(len(G)):
			if G[V_counter][i] == 1:
				stack.append(i)
		queue.append(stack.pop())



		print("stack: ", stack)
		print("queue: ", queue)
		print("cycle_counter", cycle_counter)
		r.pop()




	print("V-cntr pverflow: ", V_counter)
	print(G[0][1])
	print(G[0][4])
	print(G[1][0])
	print(G[1][2])
	print(G[1][4])
	print(G[2][1])
	print(G[2][3])
	print(G[3][2])
	print(G[3][4])
	print(G[3][5])
	print(G[4][0])
	print(G[4][1])
	print(G[4][3])
	print(G[5][3])







def solution():
	data = loadDataArray()
	datastr = loadDataString()
	start = data[0]
	finish = data[1]
	G = makeGraph(data, datastr)
	computations(G, start, finish)


if __name__ == "__main__":
	solution()