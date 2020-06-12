# Списки смежности, классический способ
def repFirst():
	# 0	 1  2  3  4  5  6  7
	# a, b, c, d, e, f, g, h
	a, b, c, d, e, f, g, h = range(8)

	N = [
		{b, c, d, e, f}, # a
		{c, e}, # b
		{d}, # c
		{e}, # d
		{f}, # e
		{c, g, h}, # f
		{f, h}, # g
		{f, g} # h
	]

	print( b in N[a] ) # смежная ?
	print( len(N[f]) ) # степень
	print(N[0])

# Массив смежности, в некоторых случаях меньше накладных расходов
def repSecond():
	a, b, c, d, e, f, g, h = range(8)
	N = [
		[b, c, d, e, f],  # a
		[c, e],  # b
		[d],  # c
		[e],  # d
		[f],  # e
		[c, g, h],  # f
		[f, h],  # g
		[f, g]  # h
	]

	print(c in N[a])  # смежная ?
	print(len(N[a]))  # степень
	print(N[1])


# Взвешенный список смежности
def repThird():
	a, b, c, d, e, f, g, h = range(8)
	N = [
		{b: 2, c: 1, d: 3, e: 9, f: 4},  # a
		{c: 4, e: 3},  # b
		{d: 8},  # c
		{e: 7},  # d
		{f: 5},  # e
		{c: 2, g: 2, h: 2},  # f
		{f: 1, h: 6},  # g
		{f: 9, g: 8}  # h
	]

	print(b in N[a])  # смежная ?
	print(len(N[f]))  # степень
	print(N[a][b])    # вес (a, b)

if __name__ == "__main__":
	repThird()

