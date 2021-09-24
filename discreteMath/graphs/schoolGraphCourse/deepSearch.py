# поиск в глубину

# список смежности вершин
graph = [[4, 5], [5], [3, 4], [2, 4], [0, 2, 3], [0, 1]]

# список состояния вершин
state = [False for i in range(len(graph))]

print(state)
print('Порядок обхода вершин')


def viewVertices(v):
    print(v, end = ' ')     # результат порядка обхода
    state[v] = True         # отметка о проходе по ребру
    for vertex in graph[v]:
        if not state[vertex]:
            viewVertices(vertex)


for c in range(len(graph)):
    if not state[c]:
        viewVertices(c)
