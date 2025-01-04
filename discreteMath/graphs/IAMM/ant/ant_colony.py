import random
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt

def col_to_networkx(col_file_path):
    """Converts a .col file to a NetworkX graph."""
    G = nx.Graph()
    with open(col_file_path, 'r') as file:
        for line in file:
            if line.startswith('c'):
                # Comment line, ignore
                continue
            elif line.startswith('p'):
                # Problem line, initialize the graph nodes
                _, _, num_nodes, _ = line.split()
                num_nodes = int(num_nodes)
                G.add_nodes_from(range(1, num_nodes + 1))
            elif line.startswith('e'):
                # Edge line, add edges
                _, node1, node2 = line.split()
                node1, node2 = int(node1), int(node2)
                G.add_edge(node1, node2)
    return G

def heuristic(graph, node, color, colors):
    """Heuristic function: checks how many neighbors cannot be colored with the given color."""
    return 1 / (1 + sum(1 for neighbor in graph.neighbors(node) if colors[neighbor] == color))

def initialize_pheromones(graph, num_colors):
    """Initialize pheromones."""
    num_nodes = graph.number_of_nodes()
    return np.ones((num_nodes + 1, num_colors))

def select_color(graph, node, pheromones, colors, num_colors, alpha, beta):
    """Select a color for a node based on probabilities."""
    probabilities = []
    for color in range(num_colors):
        if all(colors[neighbor] != color for neighbor in graph.neighbors(node)):
            heuristic_value = heuristic(graph, node, color, colors)
            probability = (pheromones[node][color] ** alpha) * (heuristic_value ** beta)
            probabilities.append(probability)
        else:
            probabilities.append(0)
    total = sum(probabilities)
    if total == 0:
        return random.choice(range(num_colors))
    probabilities = [p / total for p in probabilities]
    return random.choices(range(num_colors), probabilities)[0]

def update_pheromones(pheromones, solutions, best_solution, evaporation_rate, q):
    """Update pheromones."""
    pheromones *= (1 - evaporation_rate)
    for solution in solutions:
        for node, color in enumerate(solution, start=1):
            pheromones[node][color] += q / len(solution)
    for node, color in enumerate(best_solution, start=1):
        pheromones[node][color] += q

def ant_colony_coloring(graph, num_colors, alpha=1, beta=2, evaporation_rate=0.5, q=100, num_ants=10, max_iter=100):
    """Ant colony algorithm for graph coloring."""
    num_nodes = graph.number_of_nodes()
    pheromones = initialize_pheromones(graph, num_colors)
    best_solution = None
    best_colors_used = float('inf')

    for _ in range(max_iter):
        solutions = []
        for _ in range(num_ants):
            colors = [-1] * (num_nodes + 1)
            for node in range(1, num_nodes + 1):
                color = select_color(graph, node, pheromones, colors, num_colors, alpha, beta)
                colors[node] = color
            solutions.append(colors[1:])

        # Find the best solution
        for solution in solutions:
            colors_used = len(set(solution))
            if colors_used < best_colors_used:
                best_solution = solution
                best_colors_used = colors_used

        # Update pheromones
        update_pheromones(pheromones, solutions, best_solution, evaporation_rate, q)

    return best_solution, best_colors_used

def draw_colored_graph(graph, colors):
    """Visualize the graph with colors."""
    pos = nx.spring_layout(graph)
    node_colors = [colors[node - 1] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.tab10, node_size=500, font_size=10)
    plt.show()

# Define the name of the .col file
col_file_name = "anna.col"

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the full path to the .col file
col_file_path = os.path.join(current_dir, col_file_name)

if os.path.exists(col_file_path):
    # Load graph from .col file
    graph = col_to_networkx(col_file_path)

    # Parameters for the algorithm
    num_colors = 15
    solution, colors_used = ant_colony_coloring(graph, num_colors)

    print("Best solution:", solution)
    print("Colors used:", colors_used)

    # Visualize the graph
    draw_colored_graph(graph, solution)
else:
    print(f"File not found: {col_file_path}")
