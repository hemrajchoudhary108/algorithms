from collections import defaultdict
from typing import List, Tuple

class Graph:

    def __init__(self, edges: List[Tuple[int, int]] = [], directed: bool = False) -> None:
        self.nodes = defaultdict(list)
        self.directed = directed
        self.root = None
        self.centres = []
        self.vertex = set()
        self.edge = edges
        self._build(edges)

    def __repr__(self):
        return f"Graph with {len(self.vertex)} vertices and {len(self.edges)} edges"
    
    def __getitem__(self, vertex):
        if not vertex in self.nodes:
            raise ValueError(f"Vertex {vertex} is not present in the the graph")
        return self.nodes[vertex]

    def _build(self, edges):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.nodes[u].append(v)
            self.vertex.add(u)
            self.vertex.add(v)
            if not self.directed:
                self.nodes[v].append(u)

    def children(self, vertex):
        return self.__getitem__(vertex)

    def vertexes(self):
        return self.vertex


if __name__ == '__main__':
    edges = [[1, 2], [3, 4], [5, 4], [3, 2], [3, 5]]
    graph = Graph(edges)
    print(graph.children(3))
    print(graph)