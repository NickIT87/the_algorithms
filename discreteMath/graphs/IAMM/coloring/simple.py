import networkx as nx
import os

# Define the name of the .col file
col_file_name = "example.col"

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the full path to the .col file
col_file_path = os.path.join(current_dir, col_file_name)

# Function to convert COL file to NetworkX Graph
def col_to_networkx(col_file_path):
    G = nx.Graph()
    
    with open(col_file_path, 'r') as file:
        for line in file:
            if line.startswith('c'):
                # Comment line, ignore
                continue
            elif line.startswith('p'):
                # Problem line, get the number of nodes and edges (optional for NetworkX)
                _, _, num_nodes, num_edges = line.split()
                num_nodes, num_edges = int(num_nodes), int(num_edges)
            elif line.startswith('e'):
                # Edge line, add edge between nodes
                _, node1, node2 = line.split()
                G.add_edge(int(node1), int(node2))
                
    return G

# Convert the COL file to a NetworkX graph
G = col_to_networkx(col_file_path)

# Display the graph details
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

# Optionally, visualize the graph (requires matplotlib)
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
