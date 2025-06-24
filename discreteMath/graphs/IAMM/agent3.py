import networkx as nx
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === 1. Обёртка над графом ===
class GraphAPI:
    def __init__(self, graph, start_node):
        self._graph = graph
        self._current_position = start_node

    def get_position(self):
        """Текущая вершина агента"""
        return self._current_position

    def get_neighbors(self):
        """Соседи текущей вершины"""
        return list(self._graph.neighbors(self._current_position))

    def move_to(self, node):
        """Перемещение, если возможно"""
        if node in self.get_neighbors():
            self._current_position = node
            return True
        return False

# === 2. Агент, использующий только API ===
class Agent:
    def __init__(self, api):
        self.api = api  # Агент не знает ничего о графе

    def move(self):
        """Получает соседей через API и перемещается"""
        neighbors = self.api.get_neighbors()
        if neighbors:
            next_node = random.choice(neighbors)
            self.api.move_to(next_node)

    def get_position(self):
        """Текущая позиция через API"""
        return self.api.get_position()

# === 3. Создание графа и API ===
G = nx.grid_2d_graph(5, 5)  # Сетка 5x5
pos = {node: (node[0], node[1]) for node in G.nodes()}  # Позиции узлов для визуализации

start_node = (0, 0)
api = GraphAPI(G, start_node)
agent = Agent(api)

# === 4. Анимация ===
fig, ax = plt.subplots(figsize=(5, 5))

def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", ax=ax)
    agent_position = agent.get_position()
    nx.draw_networkx_nodes(G, pos, nodelist=[agent_position], node_color="red", node_size=500, ax=ax)
    ax.set_title(f"Шаг {frame+1}, Агент в {agent_position}")
    agent.move()

ani = FuncAnimation(fig, update, frames=20, interval=500, repeat=False)
plt.show()