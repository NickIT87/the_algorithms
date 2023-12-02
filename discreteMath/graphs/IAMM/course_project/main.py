import cProfile
import pstats
import matplotlib.pyplot as plt     # type: ignore
from flowerGraph import create_flower_graph, create_custom_graph
from data import *
from alglib import *


def print_data(G):
    # Set the node labels
    labels = nx.get_node_attributes(G, 'label')
    # Get the node colors
    try:
        node_colors = [G.nodes[node]['color'] for node in G.nodes]
    except KeyError:
        node_colors = [random_color() for _ in range(len(G.nodes)-1)]
        node_colors.insert(0, "red")
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
    # ============================== AK PAIR ==================================
    # print(aс_pair(G))
    # print_data(G)
    # ============================ AR REDUCTION =======================++======
    # print_data(ar_nodes(G))
    # ============================== AP GRAPH =================================
    # print_data(ap_graph(testC1, testL1))
    # print_data(ap_graph(testC2, testL2))
    # MyGraph = ap_graph(testC1, testL1)
    # MyGraph = ap_graph(testC1a, testL1a, 'a')
    # print(aс_pair(MyGraph))
    # print_data(MyGraph)
    # mg = ap_graph(tgc1, tgl)
    # print_data(mg)
    # cardGraph = ap_graph(cardC, cardL, 'a')
    # print_data(cardGraph)
    # print(ac_pair(cardGraph))
    # ============================= PAIR METRICS ==============================
    # print(get_canonical_pair_metrics_from_graph(G))
    # # print_data(G)
    #
    # MyGraph = create_custom_graph(6)
    # print(get_canonical_pair_metrics_from_graph(MyGraph))
    # # print_data(MyGraph)
    #
    # edges_to_remove = [(1, 5), (1, 6)]
    # MyGraph.remove_edges_from(edges_to_remove)
    # print(get_canonical_pair_metrics_from_graph(MyGraph))
    # # print_data(MyGraph)
    #
    # BigG = create_custom_graph(9)
    # e_to_r = [(1, 5), (1, 6)]
    # BigG.remove_edges_from(e_to_r)
    # print(get_canonical_pair_metrics_from_graph(BigG))
    # # print_data(BigG)
    #
    # BigG2 = create_custom_graph(50)
    # e_to_r2 = [(1, 5), (1, 6)]
    # BigG2.remove_edges_from(e_to_r2)
    # print(get_canonical_pair_metrics_from_graph(BigG2))
    # print_data(BigG2)

    # BigG3 = create_flower_graph(num_vertices=50, path=5)
    # # e_to_r3 = [(1, 5), (1, 6)]
    # e_to_r3 = [(5, 7), (5, 18), (5, 31)]
    # BigG3.remove_edges_from(e_to_r3)
    # print(get_canonical_pair_metrics_from_graph(BigG3))
    # print_data(BigG3)
    # ============================== C PROFILER ===============================
    G = ap_graph(testC1, testL1)
    # cProfile.run('ap_graph(testC1, testL1)', filename='cprofile_results/ap_profile_results')
    # cProfile.run('ac_pair(G)', filename='ac_profile_results')
    # stats1 = pstats.Stats('cprofile_results/ac_profile_results')
    # stats2 = pstats.Stats('cprofile_results/ap_profile_results')
    # stats1.strip_dirs().sort_stats('time').print_stats()
    # stats2.strip_dirs().sort_stats('time').print_stats()
