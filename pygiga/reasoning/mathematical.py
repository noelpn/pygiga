"""
pygiga.reasoning.mathematical
=============================

Mathematical Reasoning Module

Provides basic mathematical reasoning and evaluation utilities.
"""

import math
from typing import List, Union

Number = Union[int, float]


class MathematicalReasoner:
    """
    Basic mathematical reasoning engine.
    """

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        return a / b

    def power(self, base: Number, exponent: Number) -> Number:
        return base ** exponent

    def sqrt(self, value: Number) -> float:
        return math.sqrt(value)

    def factorial(self, value: int) -> int:
        return math.factorial(value)

    def absolute(self, value: Number) -> Number:
        return abs(value)

    def maximum(self, values: List[Number]) -> Number:
        return max(values)

    def minimum(self, values: List[Number]) -> Number:
        return min(values)

    def average(self, values: List[Number]) -> float:
        if not values:
            return 0.0
        return sum(values) / len(values)

    def sum(self, values: List[Number]) -> Number:
        return sum(values)

    def evaluate(self, expression: str):
        """
        Evaluate a mathematical expression.

        Example:
            evaluate("2 + 3 * 4")
        """
        return eval(
            expression,
            {
                "__builtins__": {},
                "math": math,
            },
            {},
        )

    def __repr__(self):
        return "MathematicalReasoner()"