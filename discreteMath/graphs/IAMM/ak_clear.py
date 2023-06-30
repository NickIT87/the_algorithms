""" IAMM - Graphs - ASP Work """

import networkx as nx               # type: ignore
import matplotlib.pyplot as plt     # type: ignore
from typing import Tuple, List, Union


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
nx.draw_networkx_nodes(G, pos, node_color=node_colors, ax=ax1)  # type: ignore
nx.draw_networkx_edges(G, pos, edge_color='b', ax=ax1)
nx.draw_networkx_labels(G, pos, labels, ax=ax1)
ax1.set_title('Original Graph')

# Draw the minimum spanning tree on the second subplot (ax2)
pos = nx.spring_layout(T)  # positions for the nodes
nx.draw_networkx_nodes(T, pos, node_color=node_colors, ax=ax2)  # type: ignore
nx.draw_networkx_edges(T, pos, edge_color='b', ax=ax2)
nx.draw_networkx_labels(T, pos, ax=ax2)
ax2.set_title('Minimum Spanning Tree')

# Remove the axis ticks and labels
ax1.axis('off')
ax2.axis('off')


def ak_pair(graph: nx.Graph) -> Union[Tuple[List[str], List[str]], int, str]:
    """ get canonical pair AK """

    if len(graph.nodes) == 0:
        return 0
    elif len(graph.nodes) == 1:
        try:
            return graph.nodes[0]['label']
        except KeyError:
            return list(graph.nodes)[0]

    sigma_g: list = []
    lambda_g: list = []
    reachability_basis: list = []
    root = list(graph.nodes)[0]

    # # Find reachability basis in the graph and fill lambda_g
    ms_tree = nx.minimum_spanning_tree(graph)
    for node in ms_tree.nodes:
        node_path_labels = [ms_tree.nodes[id]['label'] 
                            for id in nx.shortest_path(
                                ms_tree, source=root, target=node)]
        reachability_basis.append(''.join(node_path_labels))
        if graph.degree(node) == 1 and node != root:
            lambda_g.append(''.join(node_path_labels))

    ni = [w for w in reachability_basis if w not in lambda_g]
    ni.pop(root)

    for q, p in enumerate(ni[1:]):
        if ni[q] not in p[:len(ni[q])]:
            qpr = ni[q] + p[::-1]
            pqr = p + ni[q][::-1]
            if qpr < pqr:
                sigma_g.append(qpr)
            else:
                sigma_g.append(pqr)

    return (sigma_g, lambda_g)


# Run function
# =============================================================================
print(ak_pair(G))

# Adjust the spacing between subplots
plt.tight_layout()
# Show the graph
#plt.show()
