"""
pygiga.memory.short_term
========================

Short Term Memory

Stores temporary information for PyGiga.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class ShortTermMemory:
    """
    Short Term Memory
    """

    def __init__(self, capacity: int = 100):

        self.capacity = capacity
        self.memory = []

    # --------------------------------------------------
    # Add
    # --------------------------------------------------

    def add(
        self,
        data: Any,
    ) -> Dict:

        item = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": data,
        }

        if len(self.memory) >= self.capacity:
            self.memory.pop(0)

        self.memory.append(item)

        return item

    # --------------------------------------------------
    # Get
    # --------------------------------------------------

    def get(
        self,
        index: int,
    ):

        if 0 <= index < len(self.memory):
            return self.memory[index]

        return None

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.memory:
            return None

        return self.memory[-1]

    # --------------------------------------------------
    # Recall
    # --------------------------------------------------

    def recall(self):

        return self.memory

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            item
            for item in self.memory
            if keyword in str(item).lower()
        ]

    # --------------------------------------------------
    # Remove Last
    # --------------------------------------------------

    def forget_last(self):

        if self.memory:
            return self.memory.pop()

        return None

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.memory.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "items": len(self.memory),
            "capacity": self.capacity,
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "ShortTermMemory",
            "items": len(self.memory),
            "capacity": self.capacity,
        }