import networkx as nx
import matplotlib.pyplot as plt


def dsatur_coloring(graph):
    # Инициализация списка цветов для всех вершин
    colors = {node: None for node in graph.nodes}
    # Массив для отслеживания насыщенности (количество уникальных цветов у соседей)
    saturation = {node: 0 for node in graph.nodes}
    # Степень вершин
    degrees = {node: len(list(graph.neighbors(node))) for node in graph.nodes}

    # Начнем с вершины с максимальной степенью
    start_node = max(degrees, key=degrees.get)
    colors[start_node] = 0  # Присваиваем первый цвет

    # Пока не все вершины раскрашены
    while None in colors.values():
        # Обновляем насыщенность для всех нераскрашенных вершин
        for node in graph.nodes:
            if colors[node] is None:
                adjacent_colors = set(colors[neighbor] for neighbor in graph.neighbors(node) if colors[neighbor] is not None)
                saturation[node] = len(adjacent_colors)

        # Выбираем вершину с максимальной насыщенностью (если несколько, выбираем с максимальной степенью)
        max_saturation = max(saturation[node] for node in graph.nodes if colors[node] is None)
        candidates = [node for node in graph.nodes if saturation[node] == max_saturation and colors[node] is None]
        next_node = max(candidates, key=lambda x: degrees[x])

        # Найти подходящий цвет для вершины
        used_colors = set(colors[neighbor] for neighbor in graph.neighbors(next_node) if colors[neighbor] is not None)
        new_color = 0
        while new_color in used_colors:
            new_color += 1

        # Присваиваем найденный цвет
        colors[next_node] = new_color

        # Убираем насыщенность для раскрашенной вершины
        saturation[next_node] = -1

    return colors


# Создание графа
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (2, 8)])

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

# Пример использования
F = nx.Graph()
F.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4)])

coloring = dsatur_coloring(G)
print("Раскраска графа (вершина: цвет):", coloring)