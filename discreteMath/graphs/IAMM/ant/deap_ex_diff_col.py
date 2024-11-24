import random
import networkx as nx
from deap import base, creator, tools, algorithms

# Создание графа с помощью NetworkX
def create_graph():
    G = nx.erdos_renyi_graph(n=10, p=0.5, seed=42)  # Генерируем случайный граф
    return G

# Функция оценки: минимизация количества цветов и предотвращение конфликтов
def evaluate(individual, graph):
    color_map = {node: individual[node] for node in graph.nodes}
    num_colors = len(set(color_map.values()))
    
    # Проверка на наличие конфликтов
    conflicts = 0
    for node1, node2 in graph.edges:
        if color_map[node1] == color_map[node2]:  # Одинаковые цвета у соседей
            conflicts += 1

    return num_colors + conflicts * len(graph.nodes),  # Целевая функция

# Настройка генетического алгоритма
def setup_ga(graph):
    # Генетический алгоритм использует минимизацию
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    
    # Индивидуум: раскраска графа (список цветов для каждой вершины)
    num_nodes = len(graph.nodes)
    toolbox.register("attr_color", random.randint, 0, num_nodes - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_color, n=num_nodes)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Операторы
    toolbox.register("evaluate", evaluate, graph=graph)
    toolbox.register("mate", tools.cxUniform, indpb=0.5)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=num_nodes - 1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox

# Основная функция
def main():
    graph = create_graph()
    toolbox = setup_ga(graph)

    # Инициализация популяции
    population = toolbox.population(n=100)
    ngen, cxpb, mutpb = 100, 0.7, 0.2

    # Запуск генетического алгоритма
    result_population, _ = algorithms.eaSimple(population, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=ngen, 
                                               stats=None, verbose=True)

    # Найти лучшее решение
    best_individual = tools.selBest(result_population, k=1)[0]
    print(f"Лучшее решение: {best_individual}")
    print(f"Целевая функция: {evaluate(best_individual, graph)}")

    # Визуализация
    color_map = [best_individual[node] for node in graph.nodes]
    nx.draw(graph, node_color=color_map, with_labels=True, cmap='tab20')
    import matplotlib.pyplot as plt
    plt.show()

if __name__ == "__main__":
    main()
