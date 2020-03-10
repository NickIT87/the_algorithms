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
    T = [[ 0 for j in range(rnum)] for i in range(rnum)]
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
    for i in G:
       print(i)
    print(start, finish)
    print(G[0][1])        # проверка ребра
    print(sum(G[0]))  # кол-во смежных вершин
    
    print(" R E F A C T O R ")
    
    # ВСЕ Переменные
    stack = []   # Стек, текущая точка
    queue = []   # Очередь
    visited = [] # Посещенные точки
    # инициализация посещенных точек в непосещенные
    for i in range(0,len(G)):
        visited.append(False) # DO REFACTOR
    cycle_counter = 0 # счетчик цикла
    adjacent_vert = 0 # количество смежных вершин
    steps = 0 # количество шагов - переходов
    needed_steps = 0 # количество необходимых шагов
    
    # Debug block
    print("-------------------------------")
    print("DEBUG BLOCK:     \n")
    print(" stack: ",stack,"\n", "queue: ",queue,"\n", "visited: ",visited)
    print(" cycle_counter: ",cycle_counter)
    print(" number adjacent_vertecies: ",adjacent_vert)
    print("STEPS: ", steps, "\n")
    print("END DEBUG BLOCK:     ")
    print("-------------------------------\n")
    # Debug block
    
    #РЕШЕНИЕ
    
    r = [1, 2, 3, 4, 5, 6]
    queue.append(start) # поместить в очередь стартовую позицию
    print("Очередь перед началом цикла: ", queue)
    # Основной цикл
    while len(r) != 0:
        cycle_counter += 1    # счетчик шагов + 1
        print("\nНачало цикла ", cycle_counter, " $$$$$$$$$$  \n")
        node = queue.pop()    # вытащить из очереди текущую точку
        stack.append(node)    # добавить в стек текущую точку
        visited[node] = True  # отметить ноду как посещенную
        
        print("текущая node: ", node)
        # проверка ноды на конечную цель
        if(node == finish):
            print("Finish NODE: ", node)
        
        # узнать количество смежных вершин в точке
        adjacent_vert = sum(G[node])
        print("adjacent vertecies counter: ",  adjacent_vert)
        
        # проверка смежных вершин и нахождение очереди точек 
        for i in range(len(G)):
            if (G[node][i] == 1) and (visited[i] == False) and (visited[i] not in queue):
                queue.append(i)
        print("текущая node: ", node)
        
       
        

        # Debug block
        print("# # # #")
        print("Cycle DEBUG BLOCK:     \n")
        print(" stack: ",stack,"\n", "queue: ",queue,"\n", "visited: ",visited)
        print(" cycle_counter: ",cycle_counter)
        print(" number adjacent_vertecies: ",adjacent_vert,)
        print("STEPS: ", steps, "\n")
        print("END DEBUG BLOCK:     ")
        print("# # # #\n")
        # Debug block

        # завершающий этап цикла
        stack.pop() # уйти из текущей точки
        steps += 1
        r.pop() # выход из цикла
        print("КОнец цикла ", cycle_counter, "  ^^^^^^^^^^^^^^^^^ \n")


    # 3 2 1 0 4 5
    print(G[3][2], G[2][1], G[1][0], G[0][4], G[4][5])
    # 1 1 1 1 0
    
    # 0 1 2 3 4 5
    print(G[0][1], G[1][2], G[2][3], G[3][4], G[4][5])
    # 1 1 1 1 0

    # 5 4 3 2 1 0
    print(G[5][4], G[4][3], G[3][2], G[2][1], G[1][0])
    # 0 1 1 1 1

            

def solution():
    data = loadDataArray()
    datastr = loadDataString()
    start = data[0]
    finish = data[1]
    G = makeGraph(data, datastr)
    computations(G, start, finish)
    
    
    sorted_points = [0, 1, 2, 3, 4, 5]
    # 0 1 2 3 4 5
    print(G[0][1], G[1][2], G[2][3], G[3][4], G[4][5])
    # 1 1 1 1 0
    answer = [G[0][1], G[1][2], G[2][3], G[3][4], G[4][5]]
    answer_number = 0
    for i in answer:
        if i == 1:
            answer_number += 1
    print(answer_number)
    


if __name__ == "__main__":
    solution()