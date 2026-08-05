"""
pygiga.knowledge.embeddings
===========================

Embedding Manager

Creates and manages vector embeddings.

Author: PyGiga
"""

import math
from typing import List, Dict


class EmbeddingManager:
    """
    Manage text embeddings.
    """

    def __init__(self):

        self.embeddings = {}

    # --------------------------------------------------
    # Generate Embedding
    # --------------------------------------------------

    def generate(
        self,
        text: str,
    ) -> List[float]:
        """
        Generate a simple embedding.

        NOTE:
        This is a placeholder implementation.
        """

        vector = []

        for character in text:

            vector.append(ord(character) / 255.0)

        return vector

    # --------------------------------------------------
    # Store
    # --------------------------------------------------

    def store(
        self,
        key: str,
        embedding: List[float],
    ):

        self.embeddings[key] = embedding

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def get(
        self,
        key: str,
    ):

        return self.embeddings.get(key)

    # --------------------------------------------------
    # Cosine Similarity
    # --------------------------------------------------

    def similarity(
        self,
        embedding1: List[float],
        embedding2: List[float],
    ) -> float:

        length = min(
            len(embedding1),
            len(embedding2),
        )

        if length == 0:
            return 0.0

        a = embedding1[:length]
        b = embedding2[:length]

        dot = sum(x * y for x, y in zip(a, b))

        magnitude_a = math.sqrt(
            sum(x * x for x in a)
        )

        magnitude_b = math.sqrt(
            sum(y * y for y in b)
        )

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot / (
            magnitude_a * magnitude_b
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def nearest(
        self,
        embedding: List[float],
    ) -> Dict:

        if not self.embeddings:
            return {}

        best_key = None
        best_score = -1

        for key, value in self.embeddings.items():

            score = self.similarity(
                embedding,
                value,
            )

            if score > best_score:

                best_score = score
                best_key = key

        return {
            "key": best_key,
            "similarity": best_score,
        }

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "stored_embeddings": len(
                self.embeddings
            )
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.embeddings.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "EmbeddingManager",
            "embeddings": len(
                self.embeddings
            ),
        }