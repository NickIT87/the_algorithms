# from pyvis.network import Network
# import networkx as nx

# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10
# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# nt = Network('500px', '500px')
# # populates the nodes and edges data structures
# nt.from_nx(nx_graph)
# #nt.show('nx.html')
# nt.toggle_physics(True)
# nt.show('mygraph.html')

from pyvis.network import Network

# Create a network instance
net = Network()

# Add nodes and edges
net.add_node(1, label="Node 1")
net.add_node(2, label="Node 2")
net.add_edge(1, 2)

# Save the network as an HTML file
net.save_graph("your_visualization.html")
