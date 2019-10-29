from collections import defaultdict, deque, namedtuple
import heapq

class Entry:
    def __init__(self, index, dist, prev=None):
        self.index = index
        self.dist = dist
        self.prev = prev
        self.valid = True

    def __lt__(self, other):
        return self.dist <= other.dist

# O(|V|^3) solution using binary heap
# def djikstra(graph, src):
    # entries = {i: Entry(i, float('inf')) for i in graph.adj.keys()}
    # entries[src].dist = 0
    # heap = list(entries.values())
    # heapq.heapify(heap)
    # while heap:
        # pivot = heapq.heappop(heap)
        # for adj, weight in graph.adj[pivot.index].items():
            # if pivot.dist + weight < entries[adj].dist:
                # entries[adj].dist = pivot.dist + weight
                # heapq.heapify(heap)
    # return { i: entry.dist for i, entry in entries.items() }

# O(|V|^2log|V|) solution using binary heap
def djikstra(graph, src):
    entries = {i: Entry(i, float('inf')) for i in graph.adj.keys()}
    entries[src].dist = 0
    heap = list(entries.values())
    heapq.heapify(heap)
    while heap:
        pivot = heapq.heappop(heap)
        if not pivot.valid: continue
        for adj, weight in graph.adj[pivot.index].items():
            if pivot.dist + weight < entries[adj].dist:
                entries[adj].valid = False
                entries[adj] = Entry(adj, pivot.dist + weight, pivot.index)
                heapq.heappush(heap, entries[adj])
    return { i: (entry.dist, entry.prev) for i, entry in entries.items() }

def recover_path(lookup, dest):
    stack = deque()
    node = dest
    while lookup[node][1] is not None:
        stack.appendleft(node)
        node = lookup[node][1]
    stack.appendleft(node)
    return stack

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
    path = recover_path(d, 6)
    print(path)
    path = recover_path(d, 8)
    print(path)
