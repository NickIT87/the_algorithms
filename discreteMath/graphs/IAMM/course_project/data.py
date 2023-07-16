import networkx as nx               # type: ignore
import random


colors = [
    'lightcoral',
    'lightblue',
    'lightgreen',
    'yellow',
    'orange',
    'magenta',
    'pink',
    'cyan'
]

def random_color():
    # Generate random RGB values
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)

    # Convert RGB to hex color
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color



G = nx.Graph()

# TEST DATA 1
# G.add_node(0, label='0', color="lightblue")
# G.add_node(1, label='1', color="lightblue")
# G.add_node(2, label='2', color="lightblue")
# G.add_node(3, label='3', color="lightblue")
# G.add_node(4, label='4', color="lightblue")
# G.add_node(5, label='5', color="lightblue")
# G.add_node(6, label='6', color="lightblue")
#
# G.add_edge(0, 1)
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(1, 4)
# G.add_edge(1, 5)
# G.add_edge(2, 3)
# G.add_edge(2, 4)
# G.add_edge(2, 5)
# G.add_edge(2, 6)
# G.add_edge(3, 4)
# G.add_edge(3, 5)
# G.add_edge(3, 6)
# G.add_edge(4, 5)
# G.add_edge(4, 6)
# G.add_edge(5, 6)

# TEST DATA 2
# G.add_node(0, label='1', color='lightcoral')
# G.add_node(1, label='2', color='lightblue')
# G.add_node(2, label='3', color='lightgreen')
# G.add_node(3, label='4', color='yellow')
# G.add_node(4, label='1', color='orange')
# G.add_node(5, label='2', color='magenta')
# G.add_node(6, label='5', color='pink')
# G.add_node(7, label='3', color='cyan')
#
# G.add_edge(0, 1)
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 3)
# G.add_edge(2, 4)
# G.add_edge(3, 4)
# G.add_edge(4, 5)
# G.add_edge(4, 6)
# G.add_edge(6, 7)

# TEST REDUCTION DATA
G.add_node(0, label='1', color='red')
G.add_node(1, label='5', color='lightgreen')
G.add_node(2, label='3', color='yellow')
G.add_node(3, label='6', color='magenta')
G.add_node(4, label='2', color='cyan')
G.add_node(5, label='5', color='orange')

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 5)
G.add_edge(5, 3)
G.add_edge(3, 4)
G.add_edge(4, 0)

# TEST DATA
# =============================================================================
testC1 = ("153521", "152431")
testL1 = ("1342531", "123241", "13412", "1523")

testC2 = ("124231",)
testL2 = ("13537", "124", "135")

testC3 = ('1251', '12431')
testL3 = ('1531', '123', '12412')
# =============================================================================