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
