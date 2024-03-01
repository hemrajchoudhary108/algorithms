class depth_first_search:
    def __init__(self,nodes = 0, graph = [[]]) -> None:
        """
        Initializes the graph with the specified number of nodes and the given adjacency matrix.

        Parameters:
            nodes (int): The number of nodes in the graph.
            graph (List[List[int]]): The adjacency matrix representing the graph.

        Returns:
            None
        """
        self.nodes = nodes
        self.graph = graph
        self.visited = set()
    
    def traverse(self, node):
        """
        Traverse the graph starting from the given node, visiting each unvisited node and its neighbors.

        Parameters:
        - node: the starting node for the traversal

        Returns:
        None
        """
        if node in self.visited:
            return
        self.visited.add(node)
        neighbours = self.graph[node]
        for neighbour in neighbours:
            # Do something Here based on requirements
            self.traverse(neighbour)


    def count_components(self):
        """
        This function counts the number of connected components in the graph.
        """
        count = 0
        for node in range(self.nodes):
            if node not in self.visited:
                self.traverse(node)
                count += 1
        self.visited = set()
        return count

