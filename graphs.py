#!/usr/bin/env python3

class Node(object):
    def __init__(self, value):
        self._value = value
        self._handled = False

class Graph(object):
    def __init__(self, data):
        self._edges = Graph.gen_adj_list(data)

    @classmethod
    def gen_adj_list(cls, data):
        edges = []
        for edge in data:
            for edge_peer in data[edge]:
                edges.append((edge, edge_peer))
        return edges

    def edges(self):
        return self._edges


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

    # print the edges of our graph (adjaceny list)
    print(g.edges())