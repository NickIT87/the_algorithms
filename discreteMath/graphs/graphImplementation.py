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


if __name__ == "__main__":
    print(N[0])

