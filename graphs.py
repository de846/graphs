#!/usr/bin/env python3
import pprint as pp

class Node(object):
    def __init__(self, value):
        self._value = value
        self._handled = False
        self._pred = None
        self._neighbors = []

    def _add_neighbor(self, other_node):
        self._neighbors.append(other_node)

    def get_neighbors(self):
        if self._neighbors:
            return self._neighbors
        else:
            return None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        print("Unable to change value of node once set")

    @property
    def handled(self):
        return self._handled

    @handled.setter
    def handled(self, value):
        if value:
            self._handled = True
        elif self._handled:
            print("This node is node handled - can't unhandle a node.")
            return

    @property
    def pred(self):
        return self._pred

    @pred.setter
    def pred(self, node):
        self._pred = node

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return "Node({})".format(self._value)

class Edge(object):
    def __init__(self, u=None, v=None, weight=1.0):
        self._u = u
        self._v = v
        self._weight = weight
        self._u._add_neighbor(self._v)

    @property
    def u(self):
        return self._u

    @property
    def v(self):
        return self._v

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value >= 0.0:
            self._weight = value

    def __repr__(self):
        return "Edge({}, {}, {})".format(self._u, self._v, self._weight)

    def __str__(self):
        return str("{}, {}".format(self._u, self._v))

class Graph(object):
    def __init__(self, data, directed=False):
        self._nodes, self._edges = self._add_nodes(data)
        self._directed = directed

    def _add_nodes(self, data):
        """
        This private method will create a dictionary of nodes for use with graph.
        :param data: input dict data passed to Graph to init
        :return: dict object with node data searchable by integer
        """
        nodes = {}
        edge_list = []
        for node in data:
            if node not in nodes:
                nodes[node] = Node(node)
            for node_edges in data[node]:
                if node_edges not in nodes:
                    nodes[node_edges] = Node(node_edges)
                edge_list.append(Edge(nodes[node], nodes[node_edges]))
        return nodes, edge_list

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    @property
    def is_directed(self):
        return self._directed

    def __len__(self):
        """
        Length of Graph should be quantity of Nodes
        :return: count of nodes
        """
        return len(self._nodes)


if __name__ == "__main__":

    # sample graph data from original course implementation to compare
    graph_data = {1: [2, 3, 4],
                  2: [9, 10],
                  3: [7, 8],
                  4: [5, 6],
                  5: [],
                  6: [],
                  7: [],
                  8: [],
                  9: [],
                  10: [11, 12],
                  11: [],
                  12: [],
    }

    g = Graph(graph_data)
