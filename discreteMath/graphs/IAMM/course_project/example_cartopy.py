import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Размер сетки (например, 10x10)
grid_size = (20, 20)

# Типы ландшафтов (кодируем числами)
land_types = {
    0: "water",   # Вода
    1: "forest",  # Лес
    2: "grass",   # Луга
    3: "mountain" # Горы
}

# Цвета для каждого типа
colors = {
    0: "blue",
    1: "green",
    2: "yellow",
    3: "gray"
}

# Генерация случайного ландшафта
np.random.seed(42)
landscape = np.random.randint(0, len(land_types), grid_size)

# Сетевые данные (например, дороги) в виде линий (x1, y1) и (x2, y2)
roads = [
    (-8, -8, -5, -5),  # Дорога от (-8, -8) до (-5, -5)
    (-6, -2, 3, 4),    # Дорога от (-6, -2) до (3, 4)
    (-4, 7, 7, -6),    # Дорога от (-4, 7) до (7, -6)
]

# Создание карты
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Добавление географических элементов
ax.set_extent([-15, 15, -15, 15])  # Условные координаты
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='red')  # Границы
ax.add_feature(cfeature.COASTLINE, edgecolor='red')  # Побережья

# Размер клетки
dx = 20 / grid_size[1]
dy = 20 / grid_size[0]

# Рисуем сетку
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        x, y = -10 + j * dx, -10 + i * dy  # Привязываем к карте
        ax.add_patch(plt.Rectangle((x, y), dx, dy, color=colors[landscape[i, j]], transform=ccrs.PlateCarree()))

# Рисуем дороги (сетевые данные)
for road in roads:
    x1, y1, x2, y2 = road
    ax.plot([x1, x2], [y1, y2], color='cyan', linewidth=2, transform=ccrs.PlateCarree())

# Добавляем легенду
from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label=land_types[0]),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label=land_types[1]),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10, label=land_types[2]),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=10, label=land_types[3]),
]

ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Добавляем координатную сетку
ax.gridlines(draw_labels=True, color='black', linestyle='--', linewidth=0.5)

plt.show()
