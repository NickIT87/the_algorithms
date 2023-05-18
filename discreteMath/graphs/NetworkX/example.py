import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes with labels
G.add_node('A', label='Node A', color='red')
G.add_node('B', label='Node B', color='blue')
G.add_node('C', label='Node C', color='green')

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Set the node labels
labels = nx.get_node_attributes(G, 'label')
# Get the node colors
node_colors = [G.nodes[node]['color'] for node in G.nodes]

T = nx.minimum_spanning_tree(G)

# Draw the graph
pos = nx.spring_layout(T)  # positions for the nodes
nx.draw_networkx_nodes(T, pos, node_color=node_colors)
nx.draw_networkx_edges(T, pos)
nx.draw_networkx_labels(T, pos, labels)

# Show the graph
plt.axis('off')
plt.show()
