import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes with labels
G.add_node('A', label='Node A')
G.add_node('B', label='Node B')
G.add_node('C', label='Node C')

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Set the node labels
labels = nx.get_node_attributes(G, 'label')

# Draw the graph
pos = nx.spring_layout(G)  # positions for the nodes
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)

# Show the graph
plt.axis('off')
plt.show()
