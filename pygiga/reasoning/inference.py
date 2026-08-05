"""
pygiga.reasoning.inference
==========================

Inference Engine

Provides a simple rule-based inference engine.
"""

from typing import Callable, Dict, List, Any


class InferenceEngine:
    """
    Basic inference engine.
    """

    def __init__(self):
        self._facts: Dict[str, Any] = {}
        self._rules: List[Callable[[Dict[str, Any]], None]] = []

    def add_fact(self, name: str, value: Any = True) -> None:
        """
        Add a fact.
        """
        self._facts[name] = value

    def remove_fact(self, name: str) -> None:
        """
        Remove a fact.
        """
        self._facts.pop(name, None)

    def has_fact(self, name: str) -> bool:
        """
        Check whether a fact exists.
        """
        return name in self._facts

    def get_fact(self, name: str, default=None):
        """
        Get a fact value.
        """
        return self._facts.get(name, default)

    def facts(self) -> Dict[str, Any]:
        """
        Return all facts.
        """
        return dict(self._facts)

    def add_rule(self, rule: Callable[[Dict[str, Any]], None]) -> None:
        """
        Add an inference rule.

        Rule signature:
            rule(facts: Dict[str, Any])
        """
        self._rules.append(rule)

    def infer(self) -> Dict[str, Any]:
        """
        Execute all inference rules.
        """
        for rule in self._rules:
            rule(self._facts)

        return self._facts

    def clear(self):
        """
        Remove all facts and rules.
        """
        self._facts.clear()
        self._rules.clear()

    def __len__(self):
        return len(self._facts)

    def __repr__(self):
        return (
            f"InferenceEngine("
            f"facts={len(self._facts)}, "
            f"rules={len(self._rules)})"
        )