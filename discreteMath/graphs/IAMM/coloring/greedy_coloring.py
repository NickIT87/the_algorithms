import networkx as nx
import matplotlib.pyplot as plt


# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Apply the greedy coloring algorithm
colors = nx.coloring.greedy_color(G, strategy="largest_first")
#colors = nx.coloring.greedy_color(G, strategy="smallest_last")
#colors = nx.coloring.greedy_color(G, strategy="independent_set")
#colors = nx.coloring.greedy_color(G, strategy="random_sequential")

# Print the colors assigned to each node
print(colors)

# Draw the graph with node colors
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=list(colors.values()), cmap=plt.cm.rainbow)
plt.show()
