#!/usr/bin/env python3

class Node(object):
    def __init__(self, value):
        self._value = value
        self._handled = False

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
        if value == True:
            self._handled = True
        elif self._handled == True:
            print("This node is node handled - can't unhandle a node.")
            return

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return "Node({})".format(self._value)

class Graph(object):
    def __init__(self, data):
        self._nodes = self._add_nodes(data)
        self._edges = self._gen_adj_list(data)

    def _add_nodes(self, data):
        nodes = set()
        for node_value in data:
            nodes.add(Node(node_value))
        return nodes

    def _gen_adj_list(self, data):
        edges = []
        for edge in data:
            for edge_peer in data[edge]:
                for known_node in self._nodes:
                    if edge_peer == known_node.value:
                        edges.append((edge, edge_peer))
                        continue
        return edges

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes

    # def __str__(self):
        # return len(self)


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
    print(len(graph_data))

    # print the edges of our graph (adjaceny list)
    print("edges of g:")
    print(g.edges)

    print("\nlooped nodes of g:")
    gnodes = g.nodes
    for gnode in gnodes:
        print(gnode)
    print("\nstr/repr of graph.nodes")
    print(gnodes)
