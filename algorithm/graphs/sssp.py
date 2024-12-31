# Single source shortest path algorithm for weighted graph using topological sorting
from algorithm.graphs.topological_sort import ToplogicalSort

class SSSP:
    def __init__(self, edges, num, start):
        tp_sort = ToplogicalSort(edges)
        tp_order = tp_sort.order
        
        graph = {i:[] for i in range(num)}
        
        for edge in edges:
            u,v,d = edge
            graph[u].append((v,d))
        
        distances = [float('inf') for _ in range(num)]
        distances[start] = 0
        previous = {}
        previous[start] = None

        for node in tp_order:
            for adj in graph[node]:
                to, edge_val = adj
                if edge_val + distances[node] < distances[to]:
                    distances[to] = edge_val + distances[node]
                    previous[to] = node
                
        self.distances = distances
        self.previous = previous


# Example usage
if __name__ == "__main__":
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (1, 3, 6),
        (1, 2, 2),
        (2, 4, 4),
        (2, 5, 2),
        (2, 3, 7),
        (3, 4, -1),
        (4, 5, -2)
    ]
    num_nodes = 6
    start_node = 1

    sssp = SSSP(edges, num_nodes, start_node)
    distances, previous = sssp.distances, sssp.previous

    if distances is not None:
        print("Distances from node", start_node)
        for node in range(num_nodes):
            print(f"Node {node}: {distances[node]}")

        print("\nPrevious nodes in the path:")
        for node in range(num_nodes):
            print(f"Node {node}: {previous[node] if node in previous else None}")
