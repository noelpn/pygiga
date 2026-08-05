"""
pygiga.memory.memory_manager
============================

Memory Manager

Coordinates all memory systems in PyGiga.

Author: PyGiga
"""

from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from .working_memory import WorkingMemory
from .episodic import EpisodicMemory
from .semantic import SemanticMemory


class MemoryManager:
    """
    Central memory manager.
    """

    def __init__(self):

        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.working_memory = WorkingMemory()
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()

    # --------------------------------------------------
    # Short-Term Memory
    # --------------------------------------------------

    def remember_short(
        self,
        data,
    ):

        return self.short_term.add(data)

    # --------------------------------------------------
    # Long-Term Memory
    # --------------------------------------------------

    def remember_long(
        self,
        key,
        data,
    ):

        return self.long_term.store(key, data)

    # --------------------------------------------------
    # Working Memory
    # --------------------------------------------------

    def remember_working(
        self,
        key,
        value,
    ):

        return self.working_memory.set(key, value)

    # --------------------------------------------------
    # Episodic Memory
    # --------------------------------------------------

    def remember_episode(
        self,
        event,
        data=None,
    ):

        return self.episodic.remember(event, data)

    # --------------------------------------------------
    # Semantic Memory
    # --------------------------------------------------

    def remember_fact(
        self,
        concept,
        value,
    ):

        return self.semantic.store(concept, value)

    # --------------------------------------------------
    # Recall
    # --------------------------------------------------

    def recall_short(self):

        return self.short_term.recall()

    def recall_long(
        self,
        key,
    ):

        return self.long_term.retrieve(key)

    def recall_working(
        self,
        key,
    ):

        return self.working_memory.get(key)

    def recall_episode(self):

        return self.episodic.recall()

    def recall_fact(
        self,
        concept,
    ):

        return self.semantic.retrieve(concept)

    # --------------------------------------------------
    # Clear All
    # --------------------------------------------------

    def clear_all(self):

        self.short_term.clear()
        self.long_term.clear()
        self.working_memory.clear()
        self.episodic.clear()
        self.semantic.clear()

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
            "module": "MemoryManager",
            "systems": [
                "ShortTermMemory",
                "LongTermMemory",
                "WorkingMemory",
                "EpisodicMemory",
                "SemanticMemory",
            ],
        }