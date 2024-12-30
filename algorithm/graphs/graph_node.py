class GraphNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.edges = []
        self.parent = None

    def add_edge(self, node):
        self.edges.append(node)

    def remove_edge(self, node):
        self.edges.remove(node)
    
    def add_parent(self, node):
        self.parent = node

    def __repr__(self):
        return str(f"GraphNode({self.value})")