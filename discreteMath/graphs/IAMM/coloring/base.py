import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)])

# Задайте кастомные цвета
custom_colors = ["red", "green", "blue", "yellow"]

# Применение алгоритма DSATUR с помощью NetworkX
coloring = nx.coloring.greedy_color(G, strategy='saturation_largest_first')

# Преобразование номеров цветов в кастомные цвета
node_colors = [custom_colors[coloring[node]] for node in G.nodes()]

# Визуализация графа
pos = nx.spring_layout(G)  # Расположение вершин для наглядности
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_color='white', font_weight='bold', font_size=10)
plt.show()
