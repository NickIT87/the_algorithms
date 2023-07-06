#!/usr/local/bin/ python3.10
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


def ar():
    """ reduction algorithm AR """
    pass


def ap(C:tuple, L:tuple, x_='1'):
    """ build graph on pair AP """
    
    # STEP 0
    G = nx.Graph()
    G.add_node(0, label=C[0][0], path=C[0][0])
    labelsDict = {}
    labelsDict[0] = G.nodes[0]['label'] + "_root"        # xi v0=x'
    
    # STEP 1
    # for loop ... in progress ...    
    for i in range(1, len(C[0])-1):
        G.add_node(i, label=C[0][i], path=None)
        labelsDict[i] = C[0][i]
        G.add_edge(i-1, i)
        if (i == len(C[0])-2):
            G.add_edge(i, 0)
    #ar(G)
    
    print(G.nodes.data())
    
# =============================================================================
#     for i in range(0, len(C[0])-2):
#         print(i)
#         G.add_edge(i, i+1)
#         if i == len(C[0])-3:
#             G.add_edge(i+1, 0)
# =============================================================================

# =============================================================================
#     print(G.nodes.data())
#     print(G.nodes)
#     print(G._node[0])
#     print(G._node)
# =============================================================================
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Draw the original graph on the first subplot (ax1)
    pos = nx.spring_layout(G)  # positions for the nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', ax=ax1)  # type: ignore
    nx.draw_networkx_edges(G, pos, edge_color='b', ax=ax1)
    nx.draw_networkx_labels(G, pos, labelsDict, ax=ax1)
    ax1.set_title('labeled Graph')

    # Draw the minimum spanning tree on the second subplot (ax2)
    pos = nx.spring_layout(G)  # positions for the nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', ax=ax2)  # type: ignore
    nx.draw_networkx_edges(G, pos, edge_color='b', ax=ax2)
    nx.draw_networkx_labels(G, pos, ax=ax2)
    ax2.set_title('id graph')

    # Remove the axis ticks and labels
    ax1.axis('off')
    ax2.axis('off')

    # Adjust the spacing between subplots
    plt.tight_layout()
    # Show the graph
    plt.show()


# TEST DATA
# =============================================================================
# cycles
testC1 = ("153521", "152431")
# leafs
testL1 = ("1342531", "123241", "13412", "1523")
# =============================================================================

# run function
# =============================================================================
ap(testC1, testL1)
