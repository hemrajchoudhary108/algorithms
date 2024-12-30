from collections import defaultdict

class ToplogicalSort:
    def __init__(self, edges): # Edges should be directed
        self.edges = edges
        self.graph = defaultdict(list)
        self._build()
        self._sort()

    def _build(self):
        for edge in self.edges:
            u, v = edge
            self.graph[u].append(v)
        print('Build complete')

    def _dfs(self, at, visited, order):
        visited.add(at)
        if not at in self.graph:
            order.append(at)
            return
        for to in self.graph[at]:
            if not to in visited:
                self._dfs(to, visited, order)
        order.append(at)

    def _sort(self):
        print('Sorting started')
        order = []
        visited = set()
        nodes = self.graph.keys()
        for node in nodes:
            if not node in visited:
                self._dfs(node, visited, order)
        self.order = order[::-1]


if __name__ == '__main__':
    edges = [
        (1, 2), (1, 3), 
        (2, 4), (2, 5), 
        (3, 4), (3, 5)
    ]
    sort = ToplogicalSort(edges)
    print(sort.order)