from heapq import heappush, heappop
class Dijkstra:
    def __init__(self, graph, n, start):
        self.graph = graph
        self.n = n
        self.start = start 
    
    def lazy_implementation(self):
        visited = [False] * self.n
        distance = [float('inf')] * self.n 
        previous = [None] * self.n
        distance[self.start] = 0
        pq = [(0, self.start)]

        while pq:
            currentNode, nodeDistance = heappop(pq)
            
            # If visited already through some other node
            if distance[currentNode] < nodeDistance:
                continue

            for adj in self.graph.adjacent(currentNode):
                if not visited[adj]:
                    newDistance = nodeDistance + self.graph.cost((currentNode, adj))
                    if newDistance < distance[adj]:
                        distance[adj] = newDistance
                        previous[adj] = currentNode
                        heappush(pq, (newDistance, adj))
        
        return distance, previous
    

