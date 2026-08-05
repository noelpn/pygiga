"""
pygiga.reasoning.commonsense
============================

Commonsense Reasoning Module

Provides simple rule-based commonsense reasoning.
"""

from typing import Dict, List


class CommonsenseReasoner:
    """
    Basic commonsense reasoning engine.
    """

    def __init__(self):
        self._facts: Dict[str, str] = {}

    def add_fact(self, subject: str, knowledge: str) -> None:
        """
        Add a commonsense fact.

        Example:
            Bird -> Can fly
        """
        self._facts[subject.lower()] = knowledge

    def remove_fact(self, subject: str) -> None:
        """
        Remove a fact.
        """
        self._facts.pop(subject.lower(), None)

    def knows(self, subject: str) -> bool:
        """
        Check whether a fact exists.
        """
        return subject.lower() in self._facts

    def reason(self, subject: str) -> str:
        """
        Return stored commonsense knowledge.
        """
        return self._facts.get(subject.lower(), "Unknown")

    def all_facts(self) -> Dict[str, str]:
        """
        Return all stored facts.
        """
        return dict(self._facts)

    def subjects(self) -> List[str]:
        """
        Return all known subjects.
        """
        return list(self._facts.keys())

    def clear(self):
        """
        Remove all knowledge.
        """
        self._facts.clear()

    def __len__(self):
        return len(self._facts)

    def __repr__(self):
        return f"CommonsenseReasoner(facts={len(self._facts)})"