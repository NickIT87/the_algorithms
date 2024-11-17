import networkx as nx
import random
import math
import matplotlib.pyplot as plt

def generate_initial_coloring(graph, num_colors):
    """Generate an initial random coloring of the graph."""
    return {node: random.randint(0, num_colors - 1) for node in graph.nodes}

def calculate_conflicts(graph, coloring):
    """Count the number of edge conflicts in the graph given a coloring."""
    conflicts = 0
    for u, v in graph.edges:
        if coloring[u] == coloring[v]:
            conflicts += 1
    return conflicts

def get_neighbor_coloring(coloring, num_colors):
    """Generate a neighboring coloring by randomly changing the color of one node."""
    new_coloring = coloring.copy()
    node = random.choice(list(coloring.keys()))
    new_coloring[node] = random.randint(0, num_colors - 1)
    return new_coloring

def simulated_annealing(graph, num_colors, initial_temp, cooling_rate, max_steps):
    """Simulated Annealing for graph coloring."""
    # Initialize solution
    current_coloring = generate_initial_coloring(graph, num_colors)
    current_conflicts = calculate_conflicts(graph, current_coloring)
    temperature = initial_temp

    best_coloring = current_coloring.copy()
    best_conflicts = current_conflicts

    for step in range(max_steps):
        # Generate a neighboring solution
        new_coloring = get_neighbor_coloring(current_coloring, num_colors)
        new_conflicts = calculate_conflicts(graph, new_coloring)

        # Calculate acceptance probability
        delta = new_conflicts - current_conflicts
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_coloring = new_coloring
            current_conflicts = new_conflicts

        # Update the best solution found
        if current_conflicts < best_conflicts:
            best_coloring = current_coloring
            best_conflicts = current_conflicts

        # Cool down the temperature
        temperature *= cooling_rate

        # Termination condition
        if best_conflicts == 0:
            break

    return best_coloring, best_conflicts

# Generate a sample graph
# graph = nx.erdos_renyi_graph(n=10, p=0.4, seed=42)
graph = nx.Graph()
graph.add_nodes_from(range(1, 17))
graph.add_edges_from([(1, 2), (1, 4), (1, 10), (2, 3), (2, 6), (2, 11), (2, 12), (2, 13), (3, 4), (3, 5), (3, 9), (5, 6), (6, 7), (6, 8), (8, 17), (10, 11), (11, 12), (12, 13), (12, 14), (13, 14), (14, 15), (15, 16)])

# Parameters
num_colors = 3
initial_temp = 10
cooling_rate = 0.95
max_steps = 1000

# Run the algorithm
best_coloring, best_conflicts = simulated_annealing(
    graph, num_colors, initial_temp, cooling_rate, max_steps
)

# Print and visualize the result
print("Best Coloring:", best_coloring)
print("Number of Conflicts:", best_conflicts)

# Visualize the graph with coloring
node_colors = [best_coloring[node] for node in graph.nodes]
nx.draw(
    graph,
    with_labels=True,
    node_color=node_colors,
    cmap=plt.cm.Set3,
    node_size=500,
    font_color="black",
)
plt.show()
