from graphviz import Digraph

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def add_edges(graph, node):
    if node is not None:
        if node.left is not None:
            graph.edge(str(node.value), str(node.left.value))
            add_edges(graph, node.left)
        if node.right is not None:
            graph.edge(str(node.value), str(node.right.value))
            add_edges(graph, node.right)

def viz_tree(root):
    graph = Digraph()
    add_edges(graph, root)
    return graph

# Construct the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Visualize the binary tree
graph = viz_tree(root)
graph.view()

