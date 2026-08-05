"""
pygiga.memory.vector_memory
===========================

Vector Memory

Stores and retrieves vector embeddings.

Author: PyGiga
"""

import math
from datetime import datetime
from typing import Dict, List


class VectorMemory:
    """
    Vector Memory
    """

    def __init__(self):

        self.vectors = {}

    # --------------------------------------------------
    # Store
    # --------------------------------------------------

    def store(
        self,
        key: str,
        vector: List[float],
        metadata: Dict = None,
    ):

        if metadata is None:
            metadata = {}

        record = {
            "vector": vector,
            "metadata": metadata,
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.vectors[key] = record

        return record

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def retrieve(
        self,
        key: str,
    ):

        return self.vectors.get(key)

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        key: str,
    ):

        return self.vectors.pop(key, None)

    # --------------------------------------------------
    # Cosine Similarity
    # --------------------------------------------------

    def cosine_similarity(
        self,
        vector1: List[float],
        vector2: List[float],
    ) -> float:

        length = min(
            len(vector1),
            len(vector2),
        )

        if length == 0:
            return 0.0

        a = vector1[:length]
        b = vector2[:length]

        dot = sum(x * y for x, y in zip(a, b))

        mag_a = math.sqrt(sum(x * x for x in a))
        mag_b = math.sqrt(sum(y * y for y in b))

        if mag_a == 0 or mag_b == 0:
            return 0.0

        return dot / (mag_a * mag_b)

    # --------------------------------------------------
    # Nearest Search
    # --------------------------------------------------

    def nearest(
        self,
        vector: List[float],
        top_k: int = 5,
    ):

        results = []

        for key, record in self.vectors.items():

            score = self.cosine_similarity(
                vector,
                record["vector"],
            )

            results.append({
                "key": key,
                "similarity": score,
                "metadata": record["metadata"],
            })

        results.sort(
            key=lambda item: item["similarity"],
            reverse=True,
        )

        return results[:top_k]

    # --------------------------------------------------
    # Search Metadata
    # --------------------------------------------------

    def search_metadata(
        self,
        field: str,
        value,
    ):

        results = []

        for key, record in self.vectors.items():

            if record["metadata"].get(field) == value:

                results.append({
                    "key": key,
                    "record": record,
                })

        return results

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.vectors.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "vectors": len(self.vectors),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "VectorMemory",
            "vectors": len(self.vectors),
        }