#!/opt/homebrew/bin/ python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


# TEST DATA
G = nx.Graph()

G.add_node(0, label='1', color='red')
G.add_node(1, label='2', color='lightblue')
G.add_node(2, label='3', color='lightgreen')
G.add_node(3, label='4', color='yellow')
G.add_node(4, label='1', color='orange')
G.add_node(5, label='2', color='magenta')
G.add_node(6, label='5', color='pink')
G.add_node(7, label='3', color='cyan')

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(6, 7)

# Set the node labels
labels = nx.get_node_attributes(G, 'label')
# Get the node colors
node_colors = [G.nodes[node]['color'] for node in G.nodes]

T = nx.minimum_spanning_tree(G)

# Draw the graph
pos = nx.spring_layout(G)  # positions for the nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors)
nx.draw_networkx_edges(G, pos, edge_color='b')
nx.draw_networkx_labels(G, pos, labels)

# Show the graph
plt.axis('off')
plt.show()


def ak():
    """ get canonical pair AK """
    print('ak')


# run function
ak()