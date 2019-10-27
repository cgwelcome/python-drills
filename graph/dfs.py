from collections import defaultdict, deque

def discovered_dfs(graph, src):
    discovered = set([src])
    stack = deque([src])
    while stack:
        node = stack.pop()
        print(node)
        stack.extend(graph.adj[node] - discovered)
        discovered |= graph.adj[node]

class Graph:
    def __init__(self):
        self.adj = defaultdict(set)

    def add_edge(self, src, dest):
        self.adj[src].add(dest)
        self.adj[dest].add(src)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    discovered_dfs(g, 1)
