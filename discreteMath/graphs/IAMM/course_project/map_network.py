import networkx as nx
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd

# Координаты городов
cities = {
    "London": (51.5074, -0.1278),
    "Paris": (48.8566, 2.3522),
    "Berlin": (52.5200, 13.4050),
    "Madrid": (40.4168, -3.7038),
    "Rome": (41.9028, 12.4964),
    "Amsterdam": (52.3676, 4.9041),
    "Vienna": (48.2082, 16.3738),
    "Prague": (50.0755, 14.4378),
}

# Создание графа
G = nx.Graph()
for city, (lat, lon) in cities.items():
    G.add_node(city, pos=(lon, lat))  # cartopy использует (lon, lat)

# Добавление рёбер
edges = [
    ("London", "Paris"), ("Paris", "Berlin"), ("Berlin", "Amsterdam"),
    ("Madrid", "Paris"), ("Rome", "Vienna"), ("Vienna", "Berlin"),
    ("Amsterdam", "London"), ("Prague", "Berlin"), ("Prague", "Vienna")
]
G.add_edges_from(edges)

# Раскраска графа
color_map = nx.coloring.greedy_color(G, strategy="largest_first")
node_colors = [color_map[node] for node in G.nodes()]

# Отрисовка карты с высотами
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={"projection": ccrs.PlateCarree()})
ax.set_extent([-10, 20, 35, 60])  # Охват Европы

# Добавление карты высот
ax.stock_img()  # Встроенные данные высот
# ax.add_feature(cfeature.LAND, edgecolor="black")  # Суша
# ax.add_feature(cfeature.OCEAN, facecolor="lightblue")  # Океаны
ax.add_feature(cfeature.BORDERS, linestyle=":", edgecolor="red")
ax.add_feature(cfeature.COASTLINE, linewidth=1)
ax.gridlines(draw_labels=True, color='black', linestyle='--', linewidth=0.5)

# Добавляем реки с использованием встроенных данных Natural Earth
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.LAKES)

# Получение координат узлов
pos = {city: (lon, lat) for city, (lat, lon) in cities.items()}

# Рисуем граф поверх карты
nx.draw(
    G, pos, ax=ax,
    node_color=node_colors,
    with_labels=True,
    edge_color="gray",
    node_size=500,
    font_size=18,
    font_color="Red"
)

plt.title("Граф с раскраской на карте высот")
plt.show()
