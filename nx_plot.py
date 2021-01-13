import networkx as nx
import matplotlib.pyplot as plt


def plot_graph_nx(graph):
    G = nx.DiGraph()
    edges_list = []
    for edge in graph.get_all_e():
        G.add_edges_from([(edge.getSrc(), edge.getDest())], weight=edge.getWeight())

    val_map = {'A': 1.0,
               'D': 0.5714285714285714,
               'H': 0.0}

    values = ['blue' for node in G.nodes()]

    black_edges = [edge for edge in G.edges()]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                           node_color=values, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    plt.show()

