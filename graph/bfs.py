from collections import defaultdict, namedtuple, deque

def bfs(graph, src):
    discovered = defaultdict(bool)
    q = deque()
    discovered[src] = True
    q.append(src)
    while len(q) > 0:
        node = q.popleft()
        print(node)
        for adj in graph.adj[node]:
            if not discovered[adj]:
                discovered[adj] = True
                q.append(adj)


class Graph:
    def __init__(self, edges=[]):
        self.adj = defaultdict(list)
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, src, dest):
        self.adj[dest].append(src)
        self.adj[src].append(dest)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 3)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    bfs(g, 2)
