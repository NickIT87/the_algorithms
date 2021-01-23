import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node(2)
G.add_node(5)
G.add_edge(2,5)
G.add_edge(4, 1)
G.add_edges_from([(2,5),(1,3)])


print(nx.info(G))
nx.draw(G)
plt.show()