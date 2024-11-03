import networkx as nx
import tempfile

# Step 1: Create a sample COL file
col_content = """c This is a sample COL format file for a graph
p edge 5 6
e 1 2
e 1 3
e 2 3
e 2 4
e 3 5
e 4 5
"""

# Save this content to a temporary file
with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
    temp_file.write(col_content)
    col_file_path = temp_file.name  # Store file path for reading

# Step 2: Function to convert COL file to NetworkX Graph
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

# Step 3: Convert the COL file to a NetworkX graph
G = col_to_networkx(col_file_path)

# Step 4: Display the graph details
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

# Optionally, visualize the graph (requires matplotlib)
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
