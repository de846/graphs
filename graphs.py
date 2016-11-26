#!/usr/bin/env python3

class Node(object):
    def __init__(self, value):
        self._value = value
        self._handled = False

class Graph(object):
    def __init__(self, data):
        for node in data:
            print(node)
            print(data[node])


if __name__ == "__main__":
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
    print(graph_data)
    g = Graph(graph_data)