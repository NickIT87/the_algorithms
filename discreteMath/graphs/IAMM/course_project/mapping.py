import numpy as np
import matplotlib.pyplot as plt

# Размер сетки (например, 20x20)
grid_size = (20, 20)

# Типы ландшафтов (кодируем числами)
land_types = {
    0: "water",  # Вода
    1: "forest", # Лес
    2: "grass",  # Луга
    3: "mountain" # Горы
}

# Цвета для каждого типа
colors = {
    0: "blue",
    1: "green",
    2: "lightgreen",
    3: "gray"
}

# Генерация случайной карты
np.random.seed(42)
landscape = np.random.randint(0, len(land_types), grid_size)

# Визуализация карты
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xticks(range(grid_size[1] + 1))
ax.set_yticks(range(grid_size[0] + 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True, which='both', color='black', linewidth=0.5)

for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        ax.add_patch(plt.Rectangle((j, grid_size[0] - i - 1), 1, 1, color=colors[landscape[i, j]]))

plt.show()
