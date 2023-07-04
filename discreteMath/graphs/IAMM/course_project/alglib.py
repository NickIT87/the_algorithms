""" IAMM - Graphs - ASP Work """

import networkx as nx               # type: ignore
from math import ceil, sqrt
from typing import Tuple, List, Union


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
    for node in graph.nodes:
        node_path_id = nx.shortest_path(graph, source=root, target=node)
        node_path_labels = [graph.nodes[id]['label'] for id in node_path_id]
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


def formula(n: int, m: int) -> int:
    mat = ceil(3/2 + sqrt(9/4 - 2 * n + 2 * m))
    return 2 * (m - n + 1) * (n - mat + 2)
