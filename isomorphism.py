import networkx as nx


graph1 = nx.Graph()
graph1.add_nodes_from(range(1, 9))
graph1.add_edges_from([[1, 2], [1, 3], [1, 8], [2, 3], [2, 5], [3, 4], [4, 5], [4, 7], [5, 6], [6, 7], [6, 8], [7, 8]])
graph2 = nx.Graph()
graph2.add_nodes_from(range(1, 9))
graph2.add_edges_from([[1, 2], [1, 3], [1, 8], [2, 3], [2, 6], [3, 4], [4, 5], [4, 8], [5, 6], [5, 7], [6, 7], [7, 8]])
GM = nx.isomorphism.GraphMatcher(graph1, graph2)
if GM.is_isomorphic():
    print("The graphs are isomorphic.")
    print("An isomorphism between them is the following:")
    for i in graph1:
        print("v", i, "--> u", GM.mapping[i])
    print(GM.mapping)
else:
    print("The graphs are not isomorphic.")
