"""
pygiga.memory.retrieval
=======================

Memory Retrieval

Retrieves information from all memory systems.

Author: PyGiga
"""

from typing import Dict, List, Any

from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from .working_memory import WorkingMemory
from .episodic import EpisodicMemory
from .semantic import SemanticMemory


class MemoryRetrieval:
    """
    Unified memory retrieval system.
    """

    def __init__(self):

        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.working_memory = WorkingMemory()
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()

    # --------------------------------------------------
    # Individual Retrieval
    # --------------------------------------------------

    def from_short_term(self):

        return self.short_term.recall()

    def from_long_term(
        self,
        key: str,
    ):

        return self.long_term.retrieve(key)

    def from_working_memory(
        self,
        key: str,
    ):

        return self.working_memory.get(key)

    def from_episodic(self):

        return self.episodic.recall()

    def from_semantic(
        self,
        concept: str,
    ):

        return self.semantic.retrieve(concept)

    # --------------------------------------------------
    # Global Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> Dict[str, Any]:

        return {
            "short_term": self.short_term.search(keyword),
            "long_term": self.long_term.search(keyword),
            "working_memory": self.working_memory.search(keyword),
            "episodic": self.episodic.search(keyword),
            "semantic": self.semantic.search(keyword),
        }

    # --------------------------------------------------
    # Recall Everything
    # --------------------------------------------------

    def recall_all(self):

        return {
            "short_term": self.short_term.recall(),
            "long_term": self.long_term.values(),
            "working_memory": {
                key: self.working_memory.get(key)
                for key in self.working_memory.keys()
            },
            "episodic": self.episodic.recall(),
            "semantic": self.semantic.recall(),
        }

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "short_term": self.short_term.statistics(),
            "long_term": self.long_term.statistics(),
            "working_memory": self.working_memory.statistics(),
            "episodic": self.episodic.statistics(),
            "semantic": self.semantic.statistics(),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "MemoryRetrieval",
            "memory_systems": 5,
        }