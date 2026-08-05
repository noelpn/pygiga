"""
pygiga.reasoning.symbolic
=========================

Symbolic Reasoning Module

Provides basic symbolic reasoning using facts, rules,
and symbolic expressions.
"""

from typing import Callable, Dict, List, Any


class SymbolicReasoner:
    """
    Basic symbolic reasoning engine.
    """

    def __init__(self):
        self._symbols: Dict[str, Any] = {}
        self._rules: List[Callable[[Dict[str, Any]], None]] = []

    def define(self, name: str, value: Any) -> None:
        """
        Define a symbolic value.
        """
        self._symbols[name] = value

    def get(self, name: str, default=None):
        """
        Retrieve a symbolic value.
        """
        return self._symbols.get(name, default)

    def remove(self, name: str) -> None:
        """
        Remove a symbol.
        """
        self._symbols.pop(name, None)

    def exists(self, name: str) -> bool:
        """
        Check whether a symbol exists.
        """
        return name in self._symbols

    def symbols(self) -> Dict[str, Any]:
        """
        Return all defined symbols.
        """
        return dict(self._symbols)

    def add_rule(self, rule: Callable[[Dict[str, Any]], None]) -> None:
        """
        Add a symbolic reasoning rule.

        Rule signature:
            rule(symbols: Dict[str, Any])
        """
        self._rules.append(rule)

    def infer(self) -> Dict[str, Any]:
        """
        Execute all symbolic rules.
        """
        for rule in self._rules:
            rule(self._symbols)

        return self._symbols

    def evaluate(self, expression: str):
        """
        Evaluate an expression using the current symbols.

        Example:
            define("x", 10)
            evaluate("x + 5")
        """
        return eval(
            expression,
            {"__builtins__": {}},
            self._symbols,
        )

    def clear(self):
        """
        Remove all symbols and rules.
        """
        self._symbols.clear()
        self._rules.clear()

    def __len__(self):
        return len(self._symbols)

    def __repr__(self):
        return (
            f"SymbolicReasoner("
            f"symbols={len(self._symbols)}, "
            f"rules={len(self._rules)})"
        )