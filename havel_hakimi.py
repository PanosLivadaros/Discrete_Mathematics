import networkx as nx
import matplotlib.pyplot as plt


def graph_check(sequence):
    if nx.is_graphical(sequence):
        print("The sequence:", sequence, "is graphical.")
        graph = nx.havel_hakimi_graph(sequence)
        nx.draw_circular(graph, with_labels=True)
        plt.show()
    else:
        print("The sequence:", sequence, "is not graphical.")


sequence1 = [4, 1, 1, 1]
sequence2 = [2, 2, 1, 1]
graph_check(sequence1)
graph_check(sequence2)
