"""Knowledge graph."""

class KnowledgeGraph:
    """Stores graph nodes and edges."""

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, key, data=None):
        self.nodes[key] = data

    def add_edge(self, source, target):
        self.edges.append((source, target))
