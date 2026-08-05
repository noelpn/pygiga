"""Ontology manager."""

class Ontology:
    """Manages ontology terms."""

    def __init__(self):
        self.terms = {}

    def add_term(self, name, definition):
        self.terms[name] = definition
