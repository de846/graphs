#!/usr/bin/env python3


class Node(object):
    def __init__(self, value):
        self._value = value
        self._handled = False
        self._pred = None

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


class Graph(object):
    def __init__(self, data, directed=False):
        self._nodes = self._add_nodes(data)
        self._edges = self._gen_adj_list(data)
        self._directed = directed

    def _add_nodes(self, data):
        """
        This private method will create a dictionary of nodes for use with graph.
        :param data: input dict data passed to Graph to init
        :return: dict object with node data searchable by integer
        """
        nodes = {}
        for node_value in data:
            nodes[node_value] = {}
            nodes[node_value]["node_obj"] = Node(node_value)
            nodes[node_value]["node_edges"] = []
        return nodes

    def _gen_adj_list(self, data):
        """
        This private method will create the adjacency list and store them easily in the _edges attribute,
        and also within the _nodes dict so it remains easily associated with the Node object.
        :param data: input dict data passed to Graph to init
        :return: list object with edge data tuples
        """
        edges = []
        for edge in data:
            for edge_peer in data[edge]:
                if edge_peer in self._nodes.keys():
                    edges.append((edge, edge_peer))
                    self._nodes[edge]["node_edges"].append(edge_peer)
        return edges

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes

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

    print("size of graph g")
    print(len(g))

    # print the edges of our graph (adjacency list)
    print("edges of g:")
    print(g.edges)

    print("\nnodes of g:")
    gnodes = g.nodes
    print(gnodes)
