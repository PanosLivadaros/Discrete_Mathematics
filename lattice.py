import networkx as nx
import matplotlib.pyplot as plt
import math as m

nodes = 3
nodes *= nodes
edges_list = []
lattice = nx.Graph()
lattice.add_nodes_from(range(1, nodes + 1))
i = 1
while i <= nodes:
    if i <= nodes - m.sqrt(nodes):
        if i / m.sqrt(nodes) != int(i / m.sqrt(nodes)):
            edges_list.append([i, i + 1])
        edges_list.append([i, i + m.sqrt(nodes)])
    else:
        if i != nodes:
            edges_list.append([i, i + 1])
    i += 1
lattice.add_edges_from(edges_list)
nx.draw_networkx(lattice)
plt.show()
