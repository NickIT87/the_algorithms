#!/opt/homebrew/bin/ python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


def ar():
    """ reduction algorithm AR """
    pass


def ap(C:tuple, L:tuple):
    """ build graph on pair AP """
    print(C[0])

    G = nx.Graph()
    
    for i in range(0, len(C[0])-2):
        print(i)
        G.add_edge(i, i+1)
        if i == len(C[0])-3:
            G.add_edge(i+1, 0)
        
    labelsDict = {}
    labelsDict[0] = "0_1"
    labelsDict[1] = "1_5"
    labelsDict[2] = "2_3"
    labelsDict[3] = "3_5"
    labelsDict[4] = "4_2"

    print(G.nodes.data())
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
    
    print(G)


def ak():
    """ get canonical pair AK """
    pass


# TEST DATA
# cycles
testC1 = ("153521", "152431")
# leafs
testL1 = ("1342531", "123241", "13412", "1523")


# run function
ap(testC1, testL1)


# =============================================================================
# edgelist = [(1, 5), (5, 3), (3, 5), (5, 2), (2, 1)]
# 
# #el = [(1, 5), (5, 2), (2, 4), (4, 3), (3, 1)]
# 
# G = nx.Graph( edgelist )
# 
# labeldict = {}
# labeldict[1] = "3"
# labeldict[2] = "3"
# 
# print(labeldict)
# 
# nx.draw(
#     G,
#     #node_color=["red", "green", "blue", "yellow"],
#     node_color='lightgreen', 
#     edge_color='b',
#     labels=labeldict,
#     with_labels=True,
# )
# plt.show()
# =============================================================================
