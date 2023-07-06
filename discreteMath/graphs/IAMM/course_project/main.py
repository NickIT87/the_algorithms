import matplotlib.pyplot as plt     # type: ignore
from alglib import *
from data import G, testC1, testL1


def print_data(G):
    # Set the node labels
    labels = nx.get_node_attributes(G, 'label')
    # Get the node colors
    try:
        node_colors = [G.nodes[node]['color'] for node in G.nodes]
    except KeyError:
        node_colors = "lightgreen"

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

    # Adjust the spacing between subplots
    plt.tight_layout()
    # Show the graph
    plt.show()

# Run function
# =============================================================================
if __name__ == "__main__":
    #print(ak_pair(G))
    #print_data(G)
    #print(get_pair_metrics(7, 14))
    print_data(ap(testC1, testL1))