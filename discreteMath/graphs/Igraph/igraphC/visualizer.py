import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph.Read_GML("igraph_test.gml")

print(ig.summary(g))

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="circle",
    vertex_label=range(g.vcount()),
    vertex_color="lightblue"
)
plt.show()