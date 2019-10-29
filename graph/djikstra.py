from collections import defaultdict, namedtuple
import heapq

class Entry:
    def __init__(self, index, dist):
        self.index = index
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist

def djikstra(graph, src):
    entries = {i: Entry(i, float('inf')) for i in graph.adj.keys()}
    entries[src].dist = 0
    heap = list(entries.values())
    heapq.heapify(heap)
    while heap:
        pivot = heapq.heappop(heap)
        for adj, weight in graph.adj[pivot.index].items():
            if pivot.dist + weight < entries[adj].dist:
                entries[adj].dist = pivot.dist + weight
                heapq.heapify(heap)
    return { i: entry.dist for i, entry in entries.items() }

class Graph:
    def __init__(self):
        self.adj = defaultdict(dict)

    def add_edge(self, src, dest, weight):
        self.adj[src][dest] = weight
        self.adj[dest][src] = weight

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    d = djikstra(g, 0)
