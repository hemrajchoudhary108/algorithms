from algorithm.graphs import Graph

def root_tree(edges):
    """
    Given a list of edges, returns the root of the tree.
    """
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    
    root = None
    for vertex in vertices:
        is_root = True
        for edge in edges:
            if edge[1] == vertex:
                is_root = False
                break
        if is_root:
            root = vertex
            break
    return root
