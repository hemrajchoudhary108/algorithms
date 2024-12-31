from algorithm.graphs.centre import graph_center
from algorithm.graphs.graph import Graph

def ahu_encoding(graph, root, visited = set()):
    if not root:
        return ""
    visited.add(root)
    encodings = []
    for child in graph.children(root):
        if child in visited:
            continue
        
        encode = ahu_encoding(graph, child, visited)
        encodings.append(encode)
    encodings.sort()

    return '(' + ''.join(encodings) + ')'


def isomorphic(graph1, graph2) -> bool:
    center1 = graph_center(graph1)
    center2 = graph_center(graph2)

    encoding1 = ahu_encoding(graph1, center1[0])

    for center in center2:
        encoding2 = ahu_encoding(graph2, center)
        if encoding1 == encoding2:
            return True
    return False

if __name__ == '__main__':
    edges = [[1, 2], [3, 4], [5, 4], [3, 2], [3, 5]]
    graph1 = Graph(edges)
    print(ahu_encoding(graph1, 3))