""" IAMM - Graphs - ASP Work """

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

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Draw the original graph on the first subplot (ax1)
pos = nx.spring_layout(G)  # positions for the nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, ax=ax1)
nx.draw_networkx_edges(G, pos, edge_color='b', ax=ax1)
nx.draw_networkx_labels(G, pos, labels, ax=ax1)
ax1.set_title('Original Graph')

# Draw the minimum spanning tree on the second subplot (ax2)
pos = nx.spring_layout(T)  # positions for the nodes
nx.draw_networkx_nodes(T, pos, node_color=node_colors, ax=ax2)
nx.draw_networkx_edges(T, pos, edge_color='b', ax=ax2)
nx.draw_networkx_labels(T, pos, ax=ax2)
ax2.set_title('Minimum Spanning Tree')

# Remove the axis ticks and labels
ax1.axis('off')
ax2.axis('off')


def acrobatics_sort(data: list[str]) -> list[str]:
    """ sort by dictionary rules """
    trigger = True
    while trigger:
        trigger = False
        for i in range(len(data)-1):
            if len(data[i]) > len(data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                trigger = True
            if len(data[i]) == len(data[i + 1]) and data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                trigger = True
            

def ak_pair(graph) -> tuple[list[str], list[str]]:
    """ get canonical pair AK """
    sigma_g: list = []
    lambda_g: list = []
    reachability_basis: list = []

    if graph is not None and len(graph.nodes) != 0 and len(graph.nodes) == 1:
        return [graph.nodes[list(graph.nodes)[0]]['label']]

    # Find reachability basis in the graph
    ms_tree = nx.minimum_spanning_tree(graph)
    root = list(ms_tree.nodes)[0]
    for node in ms_tree.nodes:
        temp_id_basis = nx.shortest_path(ms_tree, source=root, target=node)
        temp_lbl_basis = [ms_tree.nodes[id]['label'] for id in temp_id_basis]
        reachability_basis.append(''.join(temp_lbl_basis))

    # Find all cycles in the graph
    cycles = list(nx.simple_cycles(graph))
    for cycle in cycles:
        tmp_cycle = [graph.nodes[id]['label'] for id in cycle]
        tmp_cycle.append(tmp_cycle[0])
        sigma_g.append(''.join(tmp_cycle))
        
    # Find all leaf nodes in the graph
    leaf_nodes = [node for node, degree in graph.degree() if degree == 1]
    for leaf in leaf_nodes:
        tmp_leaf = nx.shortest_path(ms_tree, source=root, target=leaf)
        if len(tmp_leaf) == 1: continue
        tmp_leaf_lbl = [ms_tree.nodes[id]['label'] for id in tmp_leaf]
        lambda_g.append(''.join(tmp_leaf_lbl))

    return (sigma_g, lambda_g)


# Run function
# =============================================================================
print(ak_pair(G))

# Adjust the spacing between subplots
plt.tight_layout()
# Show the graph
plt.show()
