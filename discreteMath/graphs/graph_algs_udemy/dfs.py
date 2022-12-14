graph = {
    0 : [1, 9],
    1 : [0, 8],
    2 : [3],
    3 : [2, 4, 5, 7],
    4 : [3],
    5 : [3, 6],
    6 : [5, 7],
    7 : [3, 6, 8, 10, 11],
    8 : [1, 7, 9],
    9 : [0, 8],
    10: [7, 11],
    11: [7, 10],
    12: [],
}

a, b, c, d, e, f, g, h = range(8)
graph2 = [
	[b, c, d, e, f],  # a
	[c, e],  # b
	[d],  # c
	[e],  # d
	[f],  # e
	[c, g, h],  # f
	[f, h],  # g
	[f, g]  # h
]

n = len(graph)
visited = [False for i in range(n)]

def dfs(at):
    if visited[at]:
        return
    visited[at] = True

    neighbours = graph[at]
    for next in neighbours:
        dfs(next)


start_node = 0
dfs(start_node)

print(visited)