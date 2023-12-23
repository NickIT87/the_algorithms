import networkx as nx
from deap import base, creator, tools
import random
import matplotlib.pyplot as plt

# Определение функции оценки
def evalNW(individual):
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if G.has_edge(i, j) and individual[i] == individual[j]:
                conflicts += 1
    return conflicts,  # return a tuple


# Определение параметров
N = 100
G = nx.gnp_random_graph(N, 0.3)

# Определение параметров алгоритма
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=N)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalNW)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Основной цикл
pop = toolbox.population(n=50)
CXPB, MUTPB, NGEN = 0.7, 0.2, 100

fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

for g in range(NGEN):
    print("-- Generation %i --" % g)

    offspring = toolbox.select(pop, len(pop))
    offspring = list(map(toolbox.clone, offspring))

    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    pop[:] = offspring

# Вывод результатов
best_ind = tools.selBest(pop, 1)[0]
print("-- Best Individual = ", best_ind)
print("-- Best Fitness = ", best_ind.fitness.values[0])

# Plot the graph
color_map = ['red', 'green', 'blue', 'yellow', 'purple']  # Define colors for the nodes
node_colors = [color_map[i] for i in best_ind]  # Assign colors to nodes

# Draw the graph
nx.draw(G, node_color=node_colors, with_labels=True)
plt.show()