import sys

from heap import Heap
from node import Node


class Graph:

    def __init__(self, directed=False):
        self._nodes = {}
        self.directed = directed

    def insert_node(self, id, x, y):
        v = Node(id, x, y)
        self._nodes[id] = v
        return v

    def insert_edge(self, from_, to, weight=0):
        if from_ not in self._nodes:
            self.insert_node(from_)
        if to not in self._nodes:
            self.insert_node(to)
        self._nodes[from_].insert_adj_node(self._nodes[to], weight)
        if not self.directed:
            self._nodes[to].insert_adj_node(self._nodes[from_], weight)

    def get_nodes(self):
        return [v for k, v in self._nodes.items()]

    def get_node(self, id):
        if id in self._nodes:
            return self._nodes[id]
        else:
            return None

    def get_edges(self):
        edges = set()
        for id, v in self._nodes.items():
            for a in v.get_adjs_nodes():
                edges.add((v, a))
        return edges

    def __iter__(self):
        return iter(self._nodes.values())

    def PrimMST(self):
        # Get the number of vertices in graph
        V = len(self._nodes)

        # key values used to pick minimum weight edge in cut
        key = []

        # List to store constructed MST
        parent = []

        # minHeap represents set E
        minHeap = Heap()

        # Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for v in self._nodes:
            parent.append(-1)
            key.append(sys.maxsize)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)

        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while not minHeap.isEmpty():

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self._nodes[u].get_adjs_nodes():

                v = pCrawl.get_id()

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and self._nodes[u].get_weight(pCrawl) < key[v]:
                    key[v] = self._nodes[u].get_weight(pCrawl)
                    parent[v] = u

                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])

        return key, parent
