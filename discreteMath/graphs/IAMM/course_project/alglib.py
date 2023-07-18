""" IAMM - Graphs - ASP Work """

import networkx as nx               # type: ignore
from math import ceil, sqrt
from typing import Tuple, List, Union, Dict
import copy

from data import random_color


def ar(G: nx.Graph) -> nx.Graph:
    """ reduction algorithm AR """

    def find_neighbours_with_the_same_labels(nghb: List, lbls: List) -> Dict:
        element_positions = {}
        for index, element in enumerate(lbls):
            if element in element_positions:
                element_positions[element].append(nghb[index])
            else:
                element_positions[element] = [nghb[index]]
        equal_elements = {
            element: positions for element,
            positions in element_positions.items() if len(positions) > 1
        }
        return equal_elements

    G_ = copy.deepcopy(G)
    trigger = True
    while trigger:
        trigger = False
        for node in G_.nodes:
            neighbors = list(G_.neighbors(node))
            labels = [G_.nodes[id]['label'] for id in neighbors]
            equals_labels = find_neighbours_with_the_same_labels(neighbors, labels)
            if equals_labels:
                for key, value in equals_labels.items():
                    not_changeble_node = min(value)
                    value.remove(not_changeble_node)
                    for v in value:
                        nghb_of_del_node = list(G_.neighbors(v))
                        nghb_of_del_node.remove(node)
                        for v_ in nghb_of_del_node:
                            G_.add_edge(v_, not_changeble_node)
                        G_.remove_node(v)
                trigger = True
                break
    return G_


def ap(C:tuple, L:tuple, x_='1') -> Union[nx.Graph, str]:
    """ build graph on pair AP """
    #print(C, L)
    def counter():
        if not hasattr(counter, 'count'):
            counter.count = 0
        counter.count += 1
        return counter.count

    def get_all_leaf_nodes_from_graph(G: nx.Graph) -> dict:
        leaf_nodes = [node for node, degree in G.degree() if degree == 1]
        node_labels = [G.nodes[id]['label'] for id in leaf_nodes]
        return {k: v for k, v in zip(leaf_nodes, node_labels)}

    # STEP 0
    q = dict()
    trash = dict()
    root = 0
    check_leaf_node = None
    G = nx.Graph()
    G.add_node(root, label=x_, color="red")

    # STEP 1
    for word in C:
        for i, l in enumerate(word[1:-1], start=1):
            #print("C1: ", i, l)
            id = counter()
            #print("C1: ", id)
            G.add_node(id, label=l, color=random_color())
            if i == 1:
                G.add_edge(root, id)
            else:
                G.add_edge(id - 1, id)
            if (i == len(word) - 2):
                G.add_edge(id, root)
        G = ar(G)

    # STEP 2
    q = get_all_leaf_nodes_from_graph(G)
    print(q)

    # STEP 3
    for word in L:
        for i, l in enumerate(word[1:], start=1):
            id = counter()
            G.add_node(id, label=l, color=random_color())
            if i == 1:
                G.add_edge(root, id)
            else:
                G.add_edge(id - 1, id)
            if i == len(word) - 1:
                check_leaf_node = id
        G = ar(G)
        if G.has_node(check_leaf_node):
            if G.degree(check_leaf_node) != 1:
                raise ValueError("Incorrect data. Graph is not exists!")
        all_leafs = get_all_leaf_nodes_from_graph(G)
        for key_id, val_label in all_leafs.items():
            if val_label != word[-1] \
                    and key_id not in q and key_id not in trash:
                q[key_id] = val_label
            else:
                trash[key_id] = val_label

    # STEP 4
    for key_id, val_label in q.items():
        all_paths = list(nx.all_simple_paths(G, source=root, target=key_id))
        all_paths_labels = ["".join([G.nodes[id]['label'] for id in path]) for path in all_paths]
        print(key_id, val_label, all_paths_labels)
        checked = False
        for w in all_paths_labels:
            for p in L:
                if w in p:
                    checked = True
        if not checked:
            print("Incorrect data. Graph is not exists!")

    return G


def check_walk(graph: nx.Graph, word: str, node_id: int, node_lbl: str, root_node: int) -> bool:

    if graph.nodes[root_node]['label'] != word[0]:
        print("label error")
        return False
    if node_lbl not in word:
        print("node_lbl not in word")
        #return False

    responce = False
    current_node = root_node
    previous_node = root_node
    check_no_backup = None

    for index, symbol in enumerate(word[1:], start=1):
        neighbors = list(graph.neighbors(current_node))
        labels = [graph.nodes[id]['label'] for id in neighbors]

        try:
            next_node = neighbors[labels.index(symbol)]
        except ValueError:
            print("No symbol in labels")
            return False

        if current_node == node_id and graph.nodes[current_node]['label'] == node_lbl:
            check_no_backup = previous_node
            print("ChecknoBackup", check_no_backup)

        if current_node == check_no_backup:
            print("current node == backup")
            return False

        print("prev, cur, next ", previous_node, current_node, next_node)

        previous_node = current_node
        current_node = next_node

        if current_node != node_id:
            return False

    responce = True

    return responce


def ak_pair(graph: nx.Graph) -> Union[Tuple[List[str], List[str]], int, str]:
    """ get canonical pair AK """

    if len(graph.nodes) == 0:
        return 0
    elif len(graph.nodes) == 1:
        try:
            return graph.nodes[0]['label']
        except KeyError:
            return list(graph.nodes)[0]

    root = list(graph.nodes)[0]
    sigma_g: list = []
    lambda_g: list = []
    reachability_basis: dict = dict()
    
    # Find reachability basis in the graph and fill lambda_g
    ms_tree = nx.minimum_spanning_tree(graph)
    for node in ms_tree.nodes:
        node_path_id = nx.shortest_path(ms_tree, source=root, target=node)
        node_path_labels = [ms_tree.nodes[id]['label'] for id in node_path_id]
        reachability_basis[''.join(node_path_labels)] = node_path_id
        if graph.degree(node) == 1 and node != root:
            lambda_g.append(''.join(node_path_labels))

    # create ni var as reachibility basis list without lambda_g values
    ni = [w for w in reachability_basis.keys() if w not in lambda_g]
    ni.pop(root)

    # Find cycles by ni and fill sigma_g
    for i, p in enumerate(ni):
        for q in ni[i+1:]:
            if p not in q[:len(p)]:
                if graph.has_edge(
                    reachability_basis[p][-1], 
                    reachability_basis[q][-1]
                ) is False:
                    continue
                pqr = p + q[::-1]
                qpr = q + p[::-1]
                if pqr < qpr:
                    sigma_g.append(pqr)
                else:
                    sigma_g.append(qpr)
   
    return (sigma_g, lambda_g)


def get_pair_metrics(n: int, m: int) -> int:
    mat = ceil(3/2 + sqrt(9/4 - 2 * n + 2 * m))
    result = 2 * (m - n + 1) * (n - mat + 2)
    return {"mat": mat, "result": result}
