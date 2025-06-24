import networkx as nx
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === 1. Кастомный связный граф ===
G = nx.Graph()
edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'),
    ('B', 'E'), ('E', 'F'), ('F', 'G'),
    ('G', 'D'), ('E', 'H'), ('H', 'I'),
    ('I', 'J'), ('J', 'G')  # Обеспечим связность и циклы
]
G.add_edges_from(edges)

# Простейшие координаты для визуализации (можно задать вручную)
pos = nx.spring_layout(G, seed=42)  # Раскладка для красивой отрисовки

# === 2. GraphAPI (как раньше) ===
class GraphAPI:
    def __init__(self, graph, start_node):
        self._graph = graph
        self._current_position = start_node

    def get_position(self):
        return self._current_position

    def get_neighbors(self):
        return list(self._graph.neighbors(self._current_position))

    def move_to(self, node):
        if node in self.get_neighbors():
            self._current_position = node
            return True
        return False

# === 3. Агент ===
class Agent:
    def __init__(self, api):
        self.api = api

    def move(self):
        neighbors = self.api.get_neighbors()
        if neighbors:
            self.api.move_to(random.choice(neighbors))

    def get_position(self):
        return self.api.get_position()

# === 4. Запуск анимации ===
start_node = 'A'
api = GraphAPI(G, start_node)
agent = Agent(api)

fig, ax = plt.subplots(figsize=(6, 6))

def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", ax=ax)
    agent_pos = agent.get_position()
    nx.draw_networkx_nodes(G, pos, nodelist=[agent_pos], node_color="red", node_size=500, ax=ax)
    ax.set_title(f"Шаг {frame+1}, Агент в {agent_pos}")
    agent.move()

ani = FuncAnimation(fig, update, frames=20, interval=500, repeat=False)
plt.show()
