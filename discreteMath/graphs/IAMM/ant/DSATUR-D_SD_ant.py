import networkx as nx
import matplotlib.pyplot as plt
import os
import random

# Define the name of the .col file
col_file_name = "dsjc500.1.col"

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the full path to the .col file
col_file_path = os.path.join(current_dir, col_file_name)

def col_to_networkx(col_file_path):
    G = nx.Graph()
    
    with open(col_file_path, 'r') as file:
        for line in file:
            if line.startswith('c'):
                # Comment line, ignore
                continue
            elif line.startswith('p'):
                # Problem line, get the number of nodes and edges (optional for NetworkX)
                _, _, num_nodes, num_edges = line.split()
                num_nodes, num_edges = int(num_nodes), int(num_edges)
                G.add_nodes_from(range(1, int(num_nodes)))
            elif line.startswith('e'):
                # Edge line, add edge between nodes
                _, node1, node2 = line.split()
                G.add_edge(int(node1), int(node2))
                
    return G

def dsatur_coloring(graph):
    print('Coloring of the original graph using the DSATUR algorithm')
    # Инициализация списка цветов для всех вершин
    colors = {node: None for node in graph.nodes}
    # Массив для отслеживания насыщенности (количество уникальных цветов у соседей)
    saturation = {node: 0 for node in graph.nodes}
    # Степень вершин
    degrees = {node: len(list(graph.neighbors(node))) for node in graph.nodes}
    #Инициализаця вершин по их рассмотрению алгоритмом в качестве текущей
    vertices_DSATUR = []

    # Начнем с вершины с максимальной степенью
    start_node = max(degrees, key=degrees.get)
    colors[start_node] = 0  # Присваиваем первый цвет
    vertices_DSATUR.append(start_node)
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
        vertices_DSATUR.append(next_node)
        # Найти подходящий цвет для вершины
        used_colors = set(colors[neighbor] for neighbor in graph.neighbors(next_node) if colors[neighbor] is not None)
        new_color = 0
        while new_color in used_colors:
            new_color += 1

        # Присваиваем найденный цвет
        colors[next_node] = new_color

        # Убираем насыщенность для раскрашенной вершины
        saturation[next_node] = -1
    print('Order of vertices considered in the DSATUR algorithm', vertices_DSATUR)
    print('Number of colors', max(colors[node] for node in graph.nodes)+1)
    return colors

def dsatur_coloring_D(graph):
        
    # создаем массив соседей длины 2 и список количества таких соседей
    Neighbors_D = {}
    degrees_D = {}
    for current_node in graph.nodes:
        distance2_current_node = []
        for neighbor_current_node in graph.neighbors(current_node):
            for neighbor_neighbor in  graph.neighbors(neighbor_current_node):
                if neighbor_neighbor not in distance2_current_node and neighbor_neighbor != current_node:
                   distance2_current_node.append(neighbor_neighbor)
        Neighbors_D[current_node] = distance2_current_node
        degrees_D[current_node] = len(distance2_current_node)
    print('D-coloring of the original graph using the DSATUR algorithm')
    #выводим список вершин графа, упорядоченный по ID
    #print ('Graph nodes by ID ', graph.nodes)
    # Инициализация списка цветов для всех вершин
    colors = {node: None for node in graph.nodes}
    # Инициализация списка цветов для всех вершин - соседей длины 2
    adjacent_D_colors = {node: None for node in graph.nodes}
    # Массив для отслеживания насыщенности (количество уникальных цветов у соседей)
    saturation_D = {node: 0 for node in graph.nodes}
    #Инициализаця вершин по их рассмотрению алгоритмом в качестве текущей
    vertices_DSATUR = []
    
    # Нахождение начальной вершины с максимальным количеством соседей длины 2
    start_node_D = max(degrees_D, key=degrees_D.get)
    #print("start_node:", list(graph.neighbors(start_node)))
    colors[start_node_D] = 0  # Присваиваем первый цвет
    saturation_D[start_node_D] = -1
    vertices_DSATUR.append(start_node_D)
    #обновление насыщения непокрашенных выршин, для покрашенных вершин оно равно -1
    while None in colors.values():
        for node in graph.nodes:
            if colors[node] is None:
                tmp_array = []
                for node1 in Neighbors_D[node]:
                    if (colors[node1] is not None) and (colors[node1] not in tmp_array):
                        tmp_array.append(colors[node1])
                adjacent_D_colors[node] = tmp_array
                saturation_D[node] = len(tmp_array)
        
        #Определение следующей вершины в качестве текущей (по насыщенности, по количеству соседей длины 2, по ID), присвоение ей насыщенности -1
        max_saturation_D = max(saturation_D[node] for node in graph.nodes if colors[node] is None)
        candidates = [node for node in graph.nodes if saturation_D[node] == max_saturation_D and colors[node] is None]
        next_node = max(candidates, key=lambda x: degrees_D[x])
        vertices_DSATUR.append(next_node)
        saturation_D[next_node] = -1
    
        #Нахождение подходящего цвета для текущей вершины и его присвоение
        tmp_array = adjacent_D_colors[next_node]
        new_color = 0
        while new_color in tmp_array:
                new_color += 1
        colors[next_node] = new_color
    print('Order of vertices considered in the DSATUR-D algorithm', vertices_DSATUR)
    print('Number of colors', max(colors[node] for node in graph.nodes)+1)
    return colors

def dsatur_coloring_SD(graph):
        
    # создаем массив соседей длины 2 и список количества таких соседей
    Neighbors_SD = {}
    degrees_SD = {}
    for current_node in graph.nodes:
        distance2_current_node = []
        for neighbor_current_node in graph.neighbors(current_node):
            if neighbor_current_node not in distance2_current_node:
                 distance2_current_node.append(neighbor_current_node)    
            for neighbor_neighbor in  graph.neighbors(neighbor_current_node):
                if neighbor_neighbor not in distance2_current_node and neighbor_neighbor != current_node:
                   distance2_current_node.append(neighbor_neighbor)
        Neighbors_SD[current_node] = distance2_current_node
        degrees_SD[current_node] = len(distance2_current_node)
    print('SD-coloring of the original graph using the DSATUR algorithm')
    #выводим список вершин графа, упорядоченный по ID
    #print ('Graph nodes by ID ', graph.nodes)
    # Инициализация списка цветов для всех вершин
    colors = {node: None for node in graph.nodes}
    # Инициализация списка цветов для всех вершин - соседей длины 2
    adjacent_SD_colors = {node: None for node in graph.nodes}
    # Массив для отслеживания насыщенности (количество уникальных цветов у соседей)
    saturation_SD = {node: 0 for node in graph.nodes}
    #Инициализаця вершин по их рассмотрению алгоритмом в качестве текущей
    vertices_DSATUR = []
    
    # Нахождение начальной вершины с максимальным количеством соседей длины 2
    start_node_SD = max(degrees_SD, key=degrees_SD.get)
    #print("start_node:", list(graph.neighbors(start_node)))
    colors[start_node_SD] = 0  # Присваиваем первый цвет
    saturation_SD[start_node_SD] = -1
    vertices_DSATUR.append(start_node_SD)
    #обновление насыщения непокрашенных выршин, для покрашенных вершин оно равно -1
    while None in colors.values():
        for node in graph.nodes:
            if colors[node] is None:
                tmp_array = []
                for node1 in Neighbors_SD[node]:
                    if (colors[node1] is not None) and (colors[node1] not in tmp_array):
                        tmp_array.append(colors[node1])
                adjacent_SD_colors[node] = tmp_array
                saturation_SD[node] = len(tmp_array)
        
        #Определение следующей вершины в качестве текущей (по насыщенности, по количеству соседей длины 2, по ID), присвоение ей насыщенности -1
        max_saturation_SD = max(saturation_SD[node] for node in graph.nodes if colors[node] is None)
        candidates = [node for node in graph.nodes if saturation_SD[node] == max_saturation_SD and colors[node] is None]
        next_node = max(candidates, key=lambda x: degrees_SD[x])
        vertices_DSATUR.append(next_node)
        saturation_SD[next_node] = -1
    
        #Нахождение подходящего цвета для текущей вершины и его присвоение
        tmp_array = adjacent_SD_colors[next_node]
        new_color = 0
        while new_color in tmp_array:
                new_color += 1
        colors[next_node] = new_color
    print('Order of vertices considered in the DSATUR-SD algorithm', vertices_DSATUR)
    print('Number of colors', max(colors[node] for node in graph.nodes)+1)
    return colors


class AntColonyGraphColoring:
    def __init__(self, graph, num_ants, alpha=1, beta=2, evaporation_rate=0.5, max_iterations=100):
        self.graph = graph
        self.num_ants = num_ants
        self.alpha = alpha  # Pheromone importance
        self.beta = beta  # Heuristic importance
        self.evaporation_rate = evaporation_rate
        self.max_iterations = max_iterations
        self.pheromone = {edge: 1 for edge in graph.edges}  # Initialize pheromones
    
    def heuristic(self, node, color, color_assignment):
        """Heuristic: Checks feasibility of color assignment."""
        for neighbor in self.graph.neighbors(node):
            if color_assignment.get(neighbor) == color:
                return 0  # Invalid if neighbor has the same color
        return 1  # Valid
    
    def color_graph(self):
        best_solution = None
        best_num_colors = float('inf')

        for iteration in range(self.max_iterations):
            solutions = []

            for _ in range(self.num_ants):
                color_assignment = {}
                for node in self.graph.nodes:
                    available_colors = []
                    for color in range(len(self.graph)):
                        if self.heuristic(node, color, color_assignment):
                            available_colors.append(color)

                    # Ant chooses color based on pheromone and heuristic
                    if available_colors:
                        probabilities = []
                        for color in available_colors:
                            # Calculate pheromone influence for the current color choice
                            pheromone_strength = 0
                            for neighbor in self.graph.neighbors(node):
                                if neighbor in color_assignment and color_assignment[neighbor] != color:
                                    pheromone_strength += self.pheromone.get((min(node, neighbor), max(node, neighbor)), 1)

                            # Adjust probability based on pheromone and heuristic
                            prob = (pheromone_strength ** self.alpha) * (1 ** self.beta)
                            probabilities.append(prob)

                        # Ensure we don't divide by zero by checking total_prob
                        total_prob = sum(probabilities)
                        if total_prob > 0:
                            probabilities = [p / total_prob for p in probabilities]
                            color = random.choices(available_colors, probabilities)[0]
                        else:
                            # If no pheromone influence, select a random color
                            color = random.choice(available_colors)

                        color_assignment[node] = color
                    else:
                        # If no available colors (shouldn't happen if heuristic is correct), assign a new color
                        color_assignment[node] = max(color_assignment.values(), default=0) + 1

                solutions.append(color_assignment)

            # Update pheromones based on solutions
            self._update_pheromones(solutions)

            # Check for the best solution
            for solution in solutions:
                num_colors = len(set(solution.values()))
                if num_colors < best_num_colors:
                    best_solution = solution
                    best_num_colors = num_colors

            print(f"Iteration {iteration + 1}: Best solution uses {best_num_colors} colors")

        return best_solution


    def _update_pheromones(self, solutions):
        # Evaporate existing pheromones
        for edge in self.pheromone:
            self.pheromone[edge] *= (1 - self.evaporation_rate)

        # Deposit new pheromones
        for solution in solutions:
            num_colors = len(set(solution.values()))
            for node, color in solution.items():
                for neighbor in self.graph.neighbors(node):
                    if solution[neighbor] != color:  # Valid edge
                        self.pheromone[(node, neighbor)] = self.pheromone.get((node, neighbor), 0) + (1 / num_colors)


# Example usage
if __name__ == "__main__":
    # Create a sample graph
    #G = nx.erdos_renyi_graph(10, 0.5, seed=42)  # 10 nodes, 50% connectivity
    
    G = nx.Graph()
    G.add_nodes_from(range(1, 17))
    #G.add_edges_from([(1, 2), (1, 4), (1, 10), (2, 3), (2, 6), (2, 11), (2, 12), (2, 13), (3, 4), (3, 5), (3, 9), (5, 6), (6, 7), (6, 8), (8, 17), (10, 11), (11, 12), (12, 13), (12, 14), (13, 14), (14, 15), (15, 16)])
    #G.add_edges_from([(1, 3), (1, 6), (1, 11), (1, 12), (1, 13), (2, 4), (2, 5), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 6), (3, 11), (3, 12), (3, 13), (4, 5), (4, 9), (4, 10), (5, 7), (5, 8), (5, 9), (6, 11), (6, 12), (6, 13), (6, 17), (7, 8), (10, 12), (11, 12), (11, 13), (11, 14), (12, 13), (12, 14), (12, 15), (13, 14), (13, 15), (14, 16)])
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 6), (1, 10), (1, 11), (1, 12), (1, 13), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 4), (3, 5), (3, 6), (3, 9), (3, 11), (3, 12), (3, 13), (4, 5), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 11), (6, 12), (6, 13), (6, 17), (7, 8), (8, 17), (10, 11), (10, 12), (11, 12), (11, 13), (11, 14), (12, 13), (12, 14), (12, 15), (13, 14), (13, 15), (14, 15), (14, 16), (15, 16)])
    # Создание графа
    # G = col_to_networkx(col_file_path)

    coloring = dsatur_coloring_SD(G)
    print("SD-coloring of the original graph (vertex: color):", coloring)
    coloring = dsatur_coloring_D(G)
    print("D-coloring of the original graph (vertex: color):", coloring)
    coloring = dsatur_coloring(G)
    print("Coloring of the original graph (vertex: color):", coloring)
    
    colony = AntColonyGraphColoring(G, num_ants=200, max_iterations=1000)
    solution = colony.color_graph()
     
    print("\nFinal Color Assignment:")
    for node, color in solution.items():
        print(f"Node {node}: Color {color}")


# Задайте кастомные цвета
##custom_colors = ["red", "green", "blue", "yellow", "black", "navy", "pink", "white", "cyan", "orange", "gray", "purple", "brown", "olive"]

# Применение алгоритма DSATUR с помощью NetworkX
##coloring = nx.coloring.greedy_color(G, strategy='saturation_largest_first')

# Преобразование номеров цветов в кастомные цвета
##node_colors = [custom_colors[coloring[node]] for node in G.nodes()]

# Визуализация графа
##pos = nx.spring_layout(G)  # Расположение вершин для наглядности
##nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_color='white', font_weight='bold', font_size=10)
##plt.show()


