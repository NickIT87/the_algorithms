# graphs representation complete

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


def solution():
	data = loadDataArray()
	datastr = loadDataString()
	start = data[0]
	finish = data[1]
	G = makeGraph(data, datastr)

	for i in G:
		print(i)

	print(start, finish)



if __name__ == "__main__":
	solution()