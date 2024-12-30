from collections import defaultdict, deque
from algorithm.graphs.graph import Graph

def graph_center(graph):
    degrees = defaultdict(int)
    for vertex in graph.vertexes():
        for child in graph.children(vertex):
            degrees[child] += 1
    
    que = deque([])
    count = 0 # This keep track of how many vertexes we have visited.
    for node, degree in degrees.items():
        if degree == 1:
            que.append(node)
            count += 1

    while count < len(graph.vertexes()):
        length = len(que)
        ind = 0
        while ind < length:
            vertex = que.popleft()
            for child in graph.children(vertex):
                degrees[child] -= 1
                if degrees[child] == 1:
                    count += 1
                    que.append(child)
            ind += 1
    return que

if __name__ == '__main__':
    edges = [[1, 2], [3, 4], [5, 4], [3, 2], [5, 6]]
    graph = Graph(edges)
    print(graph_center(graph))
