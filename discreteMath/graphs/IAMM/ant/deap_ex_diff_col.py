import random
import os
import networkx as nx
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt


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


# Создание графа с фиксированными узлами и рёбрами
def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 17))  # Узлы с 1 до 16
    G.add_edges_from([
        (1, 2), (1, 4), (1, 10),
        (2, 3), (2, 6), (2, 11), (2, 12), (2, 13),
        (3, 4), (3, 5), (3, 9),
        (5, 6), (6, 7), (6, 8), (8, 17),
        (10, 11), (11, 12), (12, 13), (12, 14),
        (13, 14), (14, 15), (15, 16)
    ])
    return G


# Функция оценки: минимизация количества цветов и предотвращение конфликтов
def evaluate(individual, graph):
    if len(individual) != len(graph.nodes):
        raise ValueError("Длина индивидуума не совпадает с числом узлов графа")
    
    color_map = {node: individual[node - 1] for node in graph.nodes}  # Узлы нумеруются с 1
    num_colors = len(set(color_map.values()))
    conflicts = sum(1 for u, v in graph.edges if color_map[u] == color_map[v])
    
    return num_colors + conflicts * len(graph.nodes),  # Целевая функция


# Настройка генетического алгоритма
def setup_ga(graph):
    # Генетический алгоритм использует минимизацию
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    
    # Индивидуум: раскраска графа (список цветов для каждой вершины)
    num_nodes = len(graph.nodes)  # Число узлов графа
    toolbox.register("attr_color", random.randint, 0, num_nodes - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_color, n=num_nodes)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Операторы
    toolbox.register("evaluate", evaluate, graph=graph)
    toolbox.register("mate", tools.cxUniform, indpb=0.5)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=num_nodes - 1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox


# Визуализация графа
def visualize_graph(graph, color_map):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, node_color=color_map, with_labels=True, cmap='tab20')
    plt.show()


# Основная функция
def main():
    
    # Define the name of the .col file
    col_file_name = "anna.col"

    # Get the current directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the full path to the .col file
    col_file_path = os.path.join(current_dir, col_file_name)
    
    #graph = create_graph()
    graph = col_to_networkx(col_file_path)
    toolbox = setup_ga(graph)

    # Инициализация популяции
    population = toolbox.population(n=100)
    ngen, cxpb, mutpb = 10000, 0.7, 0.2

    # Запуск генетического алгоритма
    result_population, _ = algorithms.eaSimple(population, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=ngen, 
                                               stats=None, verbose=True)

    # Найти лучшее решение
    best_individual = tools.selBest(result_population, k=1)[0]
    print(f"Лучшее решение: {best_individual}")
    print(f"Целевая функция: {evaluate(best_individual, graph)}")

    # Визуализация
    color_map = [best_individual[node - 1] for node in graph.nodes]
    visualize_graph(graph, color_map)


if __name__ == "__main__":
    main()
