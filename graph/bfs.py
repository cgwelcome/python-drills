from collections import defaultdict, deque

def discovered_bfs(graph, src):
    discovered = set([src])
    queue = deque([src])
    while queue:
        node = queue.popleft()
        print(node)
        queue.extend(graph.adj[node] - discovered)
        discovered |= graph.adj[node]

def visitedwithif_bfs(graph, src):
    visited = set()
    queue = deque([src])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            queue.extend(graph.adj[node] - visited);
            visited.add(node)

def visited_bfs(graph, src):
    visited = set()
    queue = deque([src])
    while queue:
        node = queue.popleft()
        print(node)
        queue.extend(graph.adj[node] - visited - set(queue));
        visited.add(node)

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
    visited_bfs(g, 1)
    visitedwithif_bfs(g, 1)
    discovered_bfs(g, 1)
