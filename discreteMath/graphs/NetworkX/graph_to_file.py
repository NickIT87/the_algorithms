import networkx as nx
from networkx.drawing.nx_pydot import to_pydot

# Create a sample graph (you can replace this with your own graph)
G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4])
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])

G.add_node(0, label="0")
G.add_node(1, label="1")
G.add_node(2, label="2")
G.add_node(3, label="3")
G.add_node(4, label="4")
G.add_node(5, label="5")
G.add_node(6, label="6")

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(2, 6)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(3, 6)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

print(G.nodes[1]['label'])

# Replace 'your_file_path.gml' with the path where you want to save the GML file
file_path = 'example.gml'

# Save the graph to a GML file
nx.write_gml(G, file_path)

dot_graph = to_pydot(G)
# Save the DOT graph to a file (optional)
dot_graph.write_dot("graph.dot")
# Alternatively, you can get the DOT representation as a string (optional)
dot_string = dot_graph.to_string()
print(dot_string)
