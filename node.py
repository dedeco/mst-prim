class Node:

    def __init__(self, id, x, y):
        self._id = id
        self._adjacent_nodes = {}
        self.coords = (x, y)
        self._visited = False
        self._previous = None

    def get_id(self):
        return self._id

    def get_coords(self):
        return self.coords

    def insert_adj_node(self, to=None, weight=0):
        self._adjacent_nodes[to] = weight

    def get_adj_nodes_ids(self):
        return self._adjacent_nodes.keys()

    def get_adjs_nodes(self):
        return self._adjacent_nodes

    def get_weight(self, to):
        return self._adjacent_nodes[to]

    def __str__(self):
        return str(self._id)
