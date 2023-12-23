import networkx as nx
from deap import base, creator, tools, algorithms
import random
import numpy
import matplotlib.pyplot as plt


# Define the problem
# We'll use a complete graph with 5 nodes
G = nx.complete_graph(5)

# Define the fitness function
def eval_coloring(individual):
    # The fitness is the number of edges that connect nodes of the same color
    fitness = 0
    for edge in G.edges:
        if individual[edge[0]] != individual[edge[1]]:
            fitness += 1
    return fitness,

# Define the individual and population
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(G.nodes))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the genetic operators
toolbox.register("evaluate", eval_coloring)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run the algorithm
pop = toolbox.population(n=50)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean)
stats.register("std", numpy.std)
stats.register("min", numpy.min)
stats.register("max", numpy.max)

pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats, halloffame=hof, verbose=True)

# Print the best solution
print("Best individual is %s, %s" % (hof[0], hof[0].fitness))

# Plot the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=hof[0])
nx.draw_networkx_edges(G, pos)
plt.show()