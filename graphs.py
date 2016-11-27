#!/usr/bin/env python3
import pprint as pp


class Node(object):
    """
    Node object which has a value, a handler, a predecessor, and peer awareness.
    """

    def __init__(self, value):
        self._value = value
        self._white = True
        self._gray = False
        self._black = False
        self._pred = None
        self._neighbors = []
        self._distance = 0

    def _add_neighbor(self, other_node):
        """
        Adds a Node object to a list
        :param other_node: Node object
        :return: None, implicit
        """
        self._neighbors.append(other_node)

    def get_neighbors(self):
        """
        Returns a list of neighbors connected by edges
        :return: list of neighbors
        """
        if self._neighbors:
            return self._neighbors
        else:
            return None

    @property
    def distance(self):
        """
        Prints value of this Node
        :return: int value of this Node
        """
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def value(self):
        """
        Prints value of this Node
        :return: int value of this Node
        """
        return self._value

    @value.setter
    def value(self, value):
        print("Unable to change value of node once set")

    @property
    def gray(self):
        return self._gray

    @gray.setter
    def gray(self, value):
        if value:
            self._gray = True
            self._white = False
        elif self._gray:
            print("Can not un-gray a Node.")

    @property
    def black(self):
        return self._black

    @black.setter
    def black(self, value):
        if value:
            self._black = True
            self._white = False
        elif self._black:
            print("Can not un-black a Node.")

    @property
    def pred(self):
        if self._pred == self:
            return -1
        else:
            return self._pred

    @pred.setter
    def pred(self, node):
        self._pred = node

    def __str__(self):
        """
        Prints value of this Node
        :return: string
        """
        return str(self._value)

    def __repr__(self):
        return "Node({})".format(self._value)


class Edge(object):
    """
    Edge object which stores left and right (u, v) pair, and weight.
    """

    def __init__(self, u=None, v=None, weight=1.0):
        self._u = u
        self._v = v
        self._weight = weight
        if u and v:
            self._u._add_neighbor(self._v)

    @property
    def u(self):
        """
        Returns the left connected Node of this Edge (u)
        :return: Node
        """
        return self._u

    @property
    def v(self):
        """
        Returns the right connected Node of this Edge (v)
        :return: Node
        """
        return self._v

    @property
    def weight(self):
        """
        Returns weight of this Edge. Default 1.0
        :return: float/int
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        if value >= 0.0:
            self._weight = value
        else:
            print("Edge weights should be positive.")

    def __repr__(self):
        return "Edge({}, {})".format(self._u, self._v)

    def __str__(self):
        return str("{}, {}".format(self._u, self._v))


class Graph(object):
    """
    Main Graph object to organize Nodes and Edges.
    """

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
        """
        Returns a dict of Nodes in this graph
        :return: dict
        """
        return self._nodes

    @property
    def edges(self):
        """
        Returns a list of Edges in this graph
        :return: list
        """
        return self._edges

    @property
    def is_directed(self):
        """
        Is this graph directed?
        :return: boolean
        """
        return self._directed

    def __len__(self):
        """
        Length of Graph should be quantity of Nodes
        :return: count of nodes
        """
        return len(self._nodes)

    def bfs(self, starting_node):
        stack = []
        current = self._nodes[starting_node]
        if current:
            print("Starting BFS at Node {}".format(current))
            stack.append(current)
            while len(stack) > 0:
                for edge in self._edges:
                    u = edge.u
                    v = edge.v
                    if current == u:
                        if not v.black:
                            v.distance = current.distance + 1
                            stack.append(v)
                    if current == v:
                        if not u.black:
                            u.distance = current.distance + 1
                            stack.append(u)

                if len(stack) > 0:
                    for stack_node in stack:
                        if not stack_node.gray:
                            stack_node.pred = current
                            stack_node.gray = True
                            print("Visited Node {}, with pred {}, and distance {}.".format(stack_node,
                                                                                           stack_node.pred,
                                                                                           stack_node.distance))
                    current.black = True
                    current = stack.pop(0)


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
    g.bfs(12)
