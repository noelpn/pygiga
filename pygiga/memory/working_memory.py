"""
pygiga.memory.working_memory
============================

Working Memory

Stores temporary information actively used
during reasoning and planning.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class WorkingMemory:
    """
    Working Memory
    """

    def __init__(self):

        self.memory = {}
        self.focus = None

    # --------------------------------------------------
    # Set
    # --------------------------------------------------

    def set(
        self,
        key: str,
        value: Any,
    ) -> Dict:

        record = {
            "value": value,
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.memory[key] = record

        return record

    # --------------------------------------------------
    # Get
    # --------------------------------------------------

    def get(
        self,
        key: str,
    ):

        if key in self.memory:
            return self.memory[key]["value"]

        return None

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def remove(
        self,
        key: str,
    ):

        return self.memory.pop(key, None)

    # --------------------------------------------------
    # Focus
    # --------------------------------------------------

    def set_focus(
        self,
        key: str,
    ):

        if key in self.memory:
            self.focus = key

    def get_focus(self):

        if self.focus is None:
            return None

        return self.memory[self.focus]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        results = []

        for key, value in self.memory.items():

            if (
                keyword in key.lower()
                or keyword in str(value["value"]).lower()
            ):

                results.append({
                    "key": key,
                    "value": value,
                })

        return results

    # --------------------------------------------------
    # Keys
    # --------------------------------------------------

    def keys(self):

        return list(self.memory.keys())

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.memory.clear()
        self.focus = None

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "items": len(self.memory),
            "focus": self.focus,
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "WorkingMemory",
            "items": len(self.memory),
            "focus": self.focus,
        }