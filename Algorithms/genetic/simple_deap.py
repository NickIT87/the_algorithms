import random
from deap import base, creator, tools, algorithms

# Определение типа оптимизации (минимизация)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Настройка инструментов для работы с генами
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)  # Генерация случайного числа в заданном диапазоне
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)  # Создание индивида
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # Создание популяции

# Определение функции для оценки качества индивида
def evaluate(individual):
    x = individual[0]
    return (x**2 - 4*x + 4,)  # Возвращаем кортеж, минимизация

# Настройка функций для эволюционного алгоритма
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Скрещивание
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Мутация
toolbox.register("select", tools.selTournament, tournsize=3)  # Выбор особей для следующего поколения

# Создание начальной популяции
population = toolbox.population(n=50)

# Запуск эволюционного алгоритма
algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, stats=None, halloffame=None, verbose=True)

# Вывод результата
best_individual = tools.selBest(population, k=1)[0]
print("Best individual:", best_individual, "Fitness:", best_individual.fitness.values)
