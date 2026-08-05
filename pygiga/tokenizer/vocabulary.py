"""Vocabulary helper."""

class Vocabulary:
    """Stores a simple token vocabulary.""

    def __init__(self):
        self.tokens = {}

    def add(self, token):
        self.tokens[token] = self.tokens.get(token, 0) + 1

    def size(self):
        return len(self.tokens)
