from pylab import *


def plot_points(x, y):
    color = (len(x) - 1) * ['m'] + ['r']
    scatter(x, y, s=100, marker='o', c=color)
    show()


def print_graph(g):
    for e in g.get_nodes():
        for a in e.get_adjs_nodes():
            print(e, a, e.get_weight(a))


from scipy.spatial import distance


def calculate_euclidean_distance(g):
    for node in g.get_nodes():
        for other_node in g.get_nodes():
            if node.get_id() != other_node.get_id():
                g.insert_edge(node.get_id(),
                              other_node.get_id(),
                              distance.euclidean(
                                  node.get_coords(),
                                  other_node.get_coords()
                              )
                              )
