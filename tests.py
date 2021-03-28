import unittest
from operator import itemgetter

from graph import Graph
from utils import plot_points, calculate_euclidean_distance


class TestCase(unittest.TestCase):

    def test01(self):
        g = Graph()

        coords = [(2, 13), (1, 19), (19, 1), (4, 17), (9, 5), (8, 1)]

        #plot_points(*[[
        #    i for i, j in coords],
        #    [j for i, j in coords]])

        for node_id, (x, y) in enumerate(coords):
            g.insert_node(node_id, x, y)

        calculate_euclidean_distance(g)

        keys, parent = g.PrimMST()

        self.assertEqual(33.6013, round(sum(keys), 4))

        l = []
        for i in range(1, len(g.get_nodes())):
            if parent[i] < i:
                l.append((parent[i], i))
            else:
                l.append((i, parent[i]))

        self.assertEqual([(0, 3),
                          (0, 4),
                          (1, 3),
                          (2, 4),
                          (4, 5)], sorted(l, key=itemgetter(0)))

    def test02(self):
        g = Graph()

        coords = [(15, 18), (11, 12), (0, 19), (19, 15), (8, 18), (0, 6)]

        #plot_points(*[[
        #    i for i, j in coords],
        #    [j for i, j in coords]])

        for node_id, (x, y) in enumerate(coords):
            g.insert_node(node_id, x, y)

        calculate_euclidean_distance(g)

        keys, parent = g.PrimMST()

        self.assertEqual(39.3004, round(sum(keys), 4))

        l = []
        for i in range(1, len(g.get_nodes())):
            if parent[i] < i:
                l.append((parent[i], i))
            else:
                l.append((i, parent[i]))

        # in lexicographical order
        self.assertEqual([(0, 3),
                          (0, 4),
                          (1, 4),
                          (1, 5),
                          (2, 4)], sorted(l, key=itemgetter(0)))

    def test03(self):
        g = Graph()

        coords = [(6, 6), (0, 0), (9, 18), (11, 0), (9, 4), (12, 13), (19, 3)]

        #plot_points(*[[
        #    i for i, j in coords],
        #    [j for i, j in coords]])

        for node_id, (x, y) in enumerate(coords):
            g.insert_node(node_id, x, y)

        calculate_euclidean_distance(g)

        keys, parent = g.PrimMST()

        self.assertEqual(40.1575, round(sum(keys), 4))

        l = []
        for i in range(1, len(g.get_nodes())):
            if parent[i] < i:
                l.append((parent[i], i))
            else:
                l.append((i, parent[i]))

        self.assertEqual([(0, 1),
                          (0, 4),
                          (0, 5),
                          (2, 5),
                          (3, 4),
                          (3, 6)], sorted(l, key=itemgetter(0)))

