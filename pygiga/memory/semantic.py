"""
pygiga.memory.semantic
======================

Semantic Memory

Stores facts, concepts, and relationships.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class SemanticMemory:
    """
    Semantic Memory
    """

    def __init__(self):

        self.knowledge = {}

    # --------------------------------------------------
    # Store Knowledge
    # --------------------------------------------------

    def store(
        self,
        concept: str,
        value: Any,
    ) -> Dict:

        record = {
            "concept": concept,
            "value": value,
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.knowledge[concept] = record

        return record

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def retrieve(
        self,
        concept: str,
    ):

        return self.knowledge.get(concept)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(
        self,
        concept: str,
        value: Any,
    ):

        if concept in self.knowledge:

            self.knowledge[concept]["value"] = value
            self.knowledge[concept]["timestamp"] = (
                datetime.utcnow().isoformat()
            )

            return self.knowledge[concept]

        return self.store(
            concept,
            value,
        )

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        concept: str,
    ):

        return self.knowledge.pop(
            concept,
            None,
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        results = []

        for concept, record in self.knowledge.items():

            if (
                keyword in concept.lower()
                or keyword in str(record["value"]).lower()
            ):

                results.append(record)

        return results

    # --------------------------------------------------
    # Concepts
    # --------------------------------------------------

    def concepts(self):

        return list(self.knowledge.keys())

    # --------------------------------------------------
    # Recall
    # --------------------------------------------------

    def recall(self):

        return list(self.knowledge.values())

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.knowledge.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "concepts": len(self.knowledge),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "SemanticMemory",
            "concepts": len(self.knowledge),
        }