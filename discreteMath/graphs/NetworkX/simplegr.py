import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

labelsDict = {}
labelsDict[0] = "0_1"
labelsDict[1] = "1_5"
labelsDict[2] = "2_3"
labelsDict[3] = "3_5"
labelsDict[4] = "4_2"

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 0)

# G.add_node('A', data="123", label="A")
# G.add_node(5)
# G.add_edge(2,5)
# G.add_edge(4, 1)
# G.add_edges_from([("A",5),(1,3)])


# print(nx.info(G))
# print(G.nodes.data())

# print(G._node["A"])

nx.draw(
    G, 
    labels=labelsDict, 
    with_labels=True,
    node_color='lightgreen',
    edge_color='b',
    node_size = 1000,
    width = 4
)
plt.show()