import networkx as nx
import matplotlib.pyplot as plt

nodes = 3
edges = []
cycle_graph = nx.Graph()
cycle_graph.add_nodes_from(range(1, nodes + 1))
i = 2
while i <= nodes + 1:
    if i == nodes + 1:
        edges.append([1, i - 1])
    else:
        edges.append([i - 1, i])
    i += 1
cycle_graph.add_edges_from(edges)
nx.draw_networkx(cycle_graph)
plt.show()
