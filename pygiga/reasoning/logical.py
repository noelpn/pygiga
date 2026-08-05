"""
pygiga.reasoning.logical
========================

Logical Reasoning Module

Provides basic propositional logic operations and rule evaluation.
"""

from typing import Callable, Dict, List, Any


class LogicalReasoner:
    """
    Basic logical reasoning engine.
    """

    def __init__(self):
        self._facts: Dict[str, bool] = {}
        self._rules: List[Callable[[Dict[str, bool]], Any]] = []

    def add_fact(self, name: str, value: bool = True) -> None:
        """
        Add a logical fact.
        """
        self._facts[name] = bool(value)

    def remove_fact(self, name: str) -> None:
        """
        Remove a logical fact.
        """
        self._facts.pop(name, None)

    def has_fact(self, name: str) -> bool:
        """
        Check if a fact exists.
        """
        return name in self._facts

    def get_fact(self, name: str, default: bool = False) -> bool:
        """
        Get the value of a fact.
        """
        return self._facts.get(name, default)

    def add_rule(self, rule: Callable[[Dict[str, bool]], Any]) -> None:
        """
        Add a logical inference rule.

        Example:
            def rule(facts):
                if facts.get("human") and facts.get("mortal") is False:
                    facts["mortal"] = True
        """
        self._rules.append(rule)

    def evaluate(self) -> Dict[str, bool]:
        """
        Execute all logical rules.
        """
        for rule in self._rules:
            rule(self._facts)

        return self._facts

    def logical_and(self, *values: bool) -> bool:
        """
        Logical AND.
        """
        return all(values)

    def logical_or(self, *values: bool) -> bool:
        """
        Logical OR.
        """
        return any(values)

    def logical_not(self, value: bool) -> bool:
        """
        Logical NOT.
        """
        return not value

    def logical_xor(self, a: bool, b: bool) -> bool:
        """
        Logical XOR.
        """
        return a != b

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
            f"LogicalReasoner("
            f"facts={len(self._facts)}, "
            f"rules={len(self._rules)})"
        )