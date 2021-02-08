from igraph import *
from igraph.drawing.graph import DefaultGraphDrawer

g = Graph.Read_GML("karate.gml")

print(summary(g))

#plot(g)

layout = g.layout_kamada_kawai()
plot(g,layout = layout)