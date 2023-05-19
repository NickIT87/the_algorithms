import networkx as nx
import matplotlib.pyplot as plt

# Initialize an empty graph
graph = nx.Graph()

# List of cycle paths
cycle_paths = [['A', 'B', 'C'], ['C', 'X', 'A']]

# List of leaf node paths
leaf_paths = [['C', 'D'], ['A', 'F'], ['C', 'F`']]

# Add cycle paths to the graph
for cycle in cycle_paths:
    for i in range(len(cycle) - 1):
        graph.add_edge(cycle[i], cycle[i+1])
    graph.add_edge(cycle[-1], cycle[0])

# Add leaf node paths to the graph
for leaf_path in leaf_paths:
    for i in range(len(leaf_path) - 1):
        graph.add_edge(leaf_path[i], leaf_path[i+1])

# Plot the graph
nx.draw(
    graph,
    with_labels=True,
    node_color='lightblue',
    node_size=500,
    font_size=10,
    font_color='black',
    edge_color='gray'
)

# Display the plot
plt.show()
