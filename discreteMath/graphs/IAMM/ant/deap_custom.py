import networkx as nx
import random
import os
from deap import base, creator, tools, algorithms

def col_to_networkx(col_file_path):
    G = nx.Graph()
    try:
        with open(col_file_path, 'r') as file:
            for line in file:
                if line.startswith('c'):
                    continue  # Комментарии игнорируются
                elif line.startswith('p'):
                    _, _, num_nodes, num_edges = line.split()
                    num_nodes = int(num_nodes)
                    G.add_nodes_from(range(1, num_nodes + 1))
                elif line.startswith('e'):
                    _, node1, node2 = line.split()
                    G.add_edge(int(node1), int(node2))
    except FileNotFoundError:
        print(f"Файл {col_file_path} не найден.")
        exit(1)
    return G

def eval_coloring(individual, graph):
    conflicts = 0
    for u, v in graph.edges():
        if individual[u - 1] == individual[v - 1]:  # Узлы начинаются с 1
            conflicts += 1
    return conflicts,

def main(graph, num_colors, population_size=100, generations=200):
    num_nodes = graph.number_of_nodes()
    
    if "FitnessMin" not in creator.__dict__:
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    if "Individual" not in creator.__dict__:
        creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_color", random.randint, 0, num_colors - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_color, n=num_nodes)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_coloring, graph=graph)
    toolbox.register("mate", tools.cxUniform, indpb=0.5)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=num_colors - 1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    
    population = toolbox.population(n=population_size)
    result, _ = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=generations, verbose=True)

    best_individual = tools.selBest(result, k=1)[0]
    return best_individual

if __name__ == "__main__":
    col_file_name = "anna.col"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    col_file_path = os.path.join(current_dir, col_file_name)
    
    G = col_to_networkx(col_file_path)
    num_colors = 3

    best_solution = main(G, num_colors)
    print("Лучшее решение (раскраска):", best_solution)
    print("Число конфликтов:", eval_coloring(best_solution, G)[0])
    
    # color_map = [f"C{color}" for color in best_solution]
    # nx.draw(G, with_labels=True, node_color=color_map, node_size=500)

    import matplotlib.pyplot as plt

    # Генерация color_map для узлов
    color_map = [f"C{best_solution[node - 1]}" for node in G.nodes()]  # Узлы нумеруются с 1

    # Отображение графа
    plt.figure(figsize=(8, 8))
    nx.draw(G, with_labels=True, node_color=color_map, node_size=500)
    plt.show()
