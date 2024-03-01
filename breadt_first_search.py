from collections import deque
class breadth_first_search:
    def __init__(self,nodes = 0, graph = [[]]) -> None:
        self.nodes = nodes
        self.graph = graph
        self.visited = set()
        self.prev = [None] * nodes

    def traverse(self):
        """
        Traverse the graph using breadth-first search and return the array of previous nodes.
        """
        prev = [None] * self.nodes
        queue = deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            if node in self.visited:
                continue
            self.visited.add(node)
            neighbours = self.graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
                prev[neighbour] = node
        return prev
        
    def reconstruct_path(self, start, end):
        """
        Reconstruct the path from the start node to the end node.
        """
        path = []
        node = end
        
        while node != start or not self.prev[node]:
            path.append(node)
            node = self.prev[node]
        if not self.prev[node]:
            return []
        path.append(start)
        path.reverse()
        return path
    

    