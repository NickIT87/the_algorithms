import networkx as nx
import random
import matplotlib.pyplot as plt
import time

class Agent:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.position = start_node  # Начальное положение агента
    
    def move(self):
        """Выбирает случайного доступного соседа и перемещается туда"""
        neighbors = list(self.graph.neighbors(self.position))
        if neighbors:
            self.position = random.choice(neighbors)
    
    def get_position(self):
        """Возвращает текущее положение агента"""
        return self.position

# Создаем граф
G = nx.grid_2d_graph(5, 5)  # Сетка 5x5
pos = {node: (node[0], node[1]) for node in G.nodes()}  # Позиции узлов для визуализации

# Инициализация агента
agent = Agent(G, (0, 0))  # Агент начинает в узле (0,0)

# Запуск симуляции движения агента
steps = 20  # Количество шагов
for i in range(steps):
    plt.figure(figsize=(5, 5))
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray")
    
    # Отображаем текущее положение агента
    agent_position = agent.get_position()
    nx.draw_networkx_nodes(G, pos, nodelist=[agent_position], node_color="red", node_size=500)
    
    plt.title(f"Шаг {i+1}, Агент в {agent_position}")
    plt.show()
    
    time.sleep(0.5)  # Пауза для визуализации
    
    # Двигаем агента
    agent.move()
