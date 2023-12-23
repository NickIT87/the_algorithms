import random

# Функция, которую мы пытаемся оптимизировать
def onemax(x):
    return sum(x)

# Генетический алгоритм
def genetic_algorithm(n, pop_size, max_gen):
    # Генерируем начальную популяцию
    population = [random.choices([0, 1], k=n) for _ in range(pop_size)]

    for gen in range(max_gen):
        # Оценка популяции
        scores = [onemax(ind) for ind in population]

        # Выбор родителей
        parents = random.choices(population, weights=[abs(score) for score in scores], k=2)

        # Кроссинговер
        child = parents[0][:n//2] + parents[1][n//2:]

        # Мутация
        if random.random() < 1/n:
            pos = random.randint(0, n-1)
            child[pos] = 1 - child[pos]

        # Замена наихудшего индивида
        worst_index = scores.index(min(scores))
        population[worst_index] = child

    # Возвращаем лучшего индивида
    scores = [onemax(ind) for ind in population]
    best_index = scores.index(max(scores))
    return population[best_index]

# Запуск алгоритма
n = 100  # Длина бинарной строки
pop_size = 100  # Размер популяции
max_gen = 100  # Максимальное количество поколений
result = genetic_algorithm(n, pop_size, max_gen)
print(result)