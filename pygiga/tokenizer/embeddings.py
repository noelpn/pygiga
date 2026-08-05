"""Embedding utilities."""

from typing import List

class EmbeddingVectorizer:
    """Generates placeholder vectors.""

    def vectorize(self, text: str):
        return [float(len(text))]

    def similarity(self, a: List[float], b: List[float]):
        return 1.0 if a == b else 0.0
