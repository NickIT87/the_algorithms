# import random
# import numpy as np
# from deap import base, creator, tools, algorithms

# # Create DEAP types
# creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# creator.create("Individual", list, fitness=creator.FitnessMax)

# # Function to evaluate an individual (neural network)
# def evaluate(individual):
#     # Convert the individual into a neural network architecture
#     # Perform training and evaluation
#     # Return the fitness (e.g., accuracy) as a tuple
#     fitness = random.random()  # Replace with actual fitness calculation
#     return fitness,

# # DEAP initialization
# toolbox = base.Toolbox()
# toolbox.register("individual", tools.initRepeat, creator.Individual, random.random, n=10)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# toolbox.register("mate", tools.cxTwoPoint)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
# toolbox.register("select", tools.selTournament, tournsize=3)
# toolbox.register("evaluate", evaluate)

# # Create the population
# population = toolbox.population(n=10)

# # Evolutionary algorithm
# generations = 5
# for gen in range(generations):
#     offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
#     fits = toolbox.map(toolbox.evaluate, offspring)
#     for fit, ind in zip(fits, offspring):
#         ind.fitness.values = fit

#     population = offspring

# # Get the best individual
# best_individual = tools.selBest(population, k=1)[0]
# print("Best individual:", best_individual)
# # Get the fitness value of the best individual
# best_fitness = best_individual.fitness.values[0]
# print("Best fitness:", best_fitness)

################################ ----------------------------------------------------------------

import random
from deap import base, creator, tools, algorithms

# Создание DEAP типов
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Функция для оценки особи (задача One Max)
def evaluate(individual):
    return sum(individual),

# Инициализация DEAP
toolbox = base.Toolbox()
toolbox.register("bit", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.bit, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Создание популяции
population = toolbox.population(n=10)

# Генетический алгоритм
generations = 5
for gen in range(generations):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit

    population = offspring

# Получение лучшей особи
best_individual = tools.selBest(population, k=1)[0]
print("Лучшая особь (бинарные биты):", best_individual)
print("Лучшая приспособленность:", best_individual.fitness.values[0])

################################ ----------------------------------------------------------------