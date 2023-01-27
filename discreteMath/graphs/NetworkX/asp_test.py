import networkx as nx
import matplotlib.pyplot as plt

edgelist = [(0, 1), (1, 2), (2, 3), (3, 0)]

G = nx.Graph( edgelist )

nx.draw(
    G, 
    #node_color=["red", "green", "blue", "yellow"],
    node_color='lightgreen', 
    edge_color='b',
    with_labels=True
)

plt.show()