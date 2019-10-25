from collections import defaultdict, namedtuple

Edge = namedtuple('Edge', ['src', 'dest'])

class Graph:
    def __init__(self, edges):
        self.adj = defaultdict(list)
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self):
        self.adj[edge.dst].append(edge.src)
        self.adj[edge.src].append(edge.dst)

