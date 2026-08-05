"""
pygiga.reasoning.causal
=======================

Causal Reasoning Module

Provides simple causal reasoning capabilities.
"""

from typing import Dict, List, Set


class CausalReasoner:
    """
    Basic causal reasoning engine.
    """

    def __init__(self):
        self._graph: Dict[str, List[str]] = {}

    def add_cause(self, cause: str, effect: str) -> None:
        """
        Register a causal relationship.

        Example:
            Rain -> Wet Ground
        """
        self._graph.setdefault(cause, []).append(effect)

    def effects_of(self, cause: str) -> List[str]:
        """
        Return direct effects of a cause.
        """
        return self._graph.get(cause, [])

    def causes_of(self, effect: str) -> List[str]:
        """
        Return all direct causes of an effect.
        """
        causes = []

        for cause, effects in self._graph.items():
            if effect in effects:
                causes.append(cause)

        return causes

    def chain(self, cause: str) -> List[str]:
        """
        Return the complete causal chain.
        """
        visited: Set[str] = set()
        result: List[str] = []

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nxt in self._graph.get(node, []):
                result.append(nxt)
                dfs(nxt)

        dfs(cause)

        return result

    def clear(self):
        """
        Remove all causal rules.
        """
        self._graph.clear()

    def __len__(self):
        return len(self._graph)

    def __repr__(self):
        return f"CausalReasoner(relations={len(self._graph)})"