# Поиск в ширину

graph = [
    [1, 3],         # 0
    [0, 3, 4, 5],   # 1
    [4, 5],         # 2
    [0, 1, 5],      # 3
    [1, 2],         # 4
    [1, 2, 3]       # 5
]

start = [-1]*len(graph)                 # список начального просмотра вершин
print('Начальное состояние: ', start)

def func(s):
    global start
    start[s] = 0                        # Начальная вершина
    queue = [s]
    print('Динамика изменения состояния вершины')
    while queue:
        print(start)
        v = queue.pop(0)
        for m in graph[v]:
            if start[m] == -1:
                queue.append(m)
                start[m] = start[v] + 1


for i in range(len(graph)):
    if start[i] == -1:
        func(i)
    print('Вершина ', i, ', номер обхода ', start[i])
