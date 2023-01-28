import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node('A', data="123", label="A")
G.add_node(5)
G.add_edge(2,5)
G.add_edge(4, 1)
G.add_edges_from([("A",5),(1,3)])


print(nx.info(G))
print(G.nodes.data())

print(G._node["A"])

nx.draw(G, with_labels=True)
plt.show()