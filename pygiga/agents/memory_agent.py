"""
pygiga.agents.memory_agent
==========================

Memory Agent

Responsible for storing and retrieving memories.

Author: PyGiga
"""

from datetime import datetime


class MemoryAgent:
    """
    Memory Agent
    """

    def __init__(self):

        self.short_term = []
        self.long_term = []

    # --------------------------------------------------
    # Store
    # --------------------------------------------------

    def store(
        self,
        memory,
        long_term=False,
    ):
        """
        Store a memory.
        """

        item = {
            "timestamp": datetime.utcnow().isoformat(),
            "memory": memory,
        }

        if long_term:
            self.long_term.append(item)
        else:
            self.short_term.append(item)

        return item

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def retrieve(self):

        """
        Return all short-term memories.
        """

        return self.short_term

    def retrieve_long_term(self):

        """
        Return all long-term memories.
        """

        return self.long_term

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.short_term:
            return None

        return self.short_term[-1]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for memory in self.short_term + self.long_term:

            if keyword in str(memory).lower():
                results.append(memory)

        return results

    # --------------------------------------------------
    # Move to Long-Term
    # --------------------------------------------------

    def consolidate(self):

        """
        Move all short-term memories into long-term memory.
        """

        self.long_term.extend(self.short_term)

        self.short_term.clear()

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def forget_last(self):

        if self.short_term:
            return self.short_term.pop()

        return None

    def clear_short_term(self):

        self.short_term.clear()

    def clear_long_term(self):

        self.long_term.clear()

    def clear(self):

        self.short_term.clear()
        self.long_term.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "short_term": len(self.short_term),
            "long_term": len(self.long_term),
            "total": len(self.short_term) + len(self.long_term),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "MemoryAgent",
            "status": "ready",
            "short_term": len(self.short_term),
            "long_term": len(self.long_term),
        }