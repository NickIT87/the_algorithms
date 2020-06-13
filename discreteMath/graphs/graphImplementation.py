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


# Словарь смежности
# Более гибкий вариант
# (позволяет использовать произвольные, хэшируемые, имена вершин)
def repFourth():
	N = {
		'a': set('bcdef'),
		'b': set('ce'),
		'c': set('d'),
		'd': set('e'),
		'e': set('f'),
		'f': set('cgh'),
		'g': set('fh'),
		'h': set('fg')
	}

	print(len(N['a']))
	print('c' in N['a'])


# adjacency matrix , матрица смежности
def repFive():
	a, b, c, d, e, f, g, h = range(8)
	# 	  a  b  c  d  e  f  g  h
	N = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
		 [0, 0, 1, 0, 1, 0, 0, 0],  # b
		 [0, 0, 0, 1, 0, 0, 0, 0],  # c
		 [0, 0, 0, 0, 1, 0, 0, 0],  # d
		 [0, 0, 0, 0, 0, 1, 0, 0],  # e
		 [0, 0, 1, 0, 0, 0, 1, 1],  # f
		 [0, 0, 0, 0, 0, 1, 0, 1],  # g
		 [0, 0, 0, 0, 0, 1, 1, 0]]  # h

	print(N[a][b])		# 1		/смежность
	print(N[b][a])		# 0
	print(sum(N[f]))	# 3		/мощность


# matrix of weights , матрица весов
def repSix():
	a, b, c, d, e, f, g, h = range(8)
	_ = float('inf')
	# 	  a  b  c  d  e  f  g  h
	W = [[0, 2, 1, 3, 9, 4, _, _],  # a
		 [_, 0, 4, _, 3, _, _, _],  # b
		 [_, _, 0, 8, _, _, _, _],  # c
		 [_, _, _, 0, 7, _, _, _],  # d
		 [_, _, _, _, 0, 5, _, _],  # e
		 [_, _, 2, _, _, 0, 2, 2],  # f
		 [_, _, _, _, _, 1, 0, 6],  # g
		 [_, _, _, _, _, 9, 8, 0]]  # h

	print(W[a][b] < _)	# Смежность
	print("float _ :", _)			# бесконечность
	print(sum(1 for w in W[a] if w < _) - 1)  # степень /мощность
	print(W[a][b])		# вес ребра




if __name__ == "__main__":
	repSix()

