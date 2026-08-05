"""
pygiga.reasoning.probablistic
=============================

Probabilistic Reasoning Module

Provides basic probability calculations and probabilistic reasoning.
"""

import math
import random
from typing import List


class ProbabilisticReasoner:
    """
    Basic probabilistic reasoning engine.
    """

    def probability(self, favorable: int, total: int) -> float:
        """
        Calculate probability.
        """
        if total <= 0:
            raise ValueError("Total outcomes must be greater than zero.")
        return favorable / total

    def complement(self, probability: float) -> float:
        """
        Calculate complementary probability.
        """
        return 1.0 - probability

    def joint(self, p_a: float, p_b: float) -> float:
        """
        Joint probability assuming independence.
        """
        return p_a * p_b

    def conditional(self, joint_probability: float, p_b: float) -> float:
        """
        Conditional probability P(A|B).
        """
        if p_b == 0:
            raise ZeroDivisionError("Probability cannot be zero.")
        return joint_probability / p_b

    def bayes(self, p_b_given_a: float,
              p_a: float,
              p_b: float) -> float:
        """
        Bayes' theorem.
        """
        if p_b == 0:
            raise ZeroDivisionError("Probability cannot be zero.")
        return (p_b_given_a * p_a) / p_b

    def normalize(self, values: List[float]) -> List[float]:
        """
        Normalize a list of probabilities.
        """
        total = sum(values)

        if total == 0:
            return [0.0 for _ in values]

        return [v / total for v in values]

    def entropy(self, probabilities: List[float]) -> float:
        """
        Calculate Shannon entropy.
        """
        entropy = 0.0

        for p in probabilities:
            if p > 0:
                entropy -= p * math.log2(p)

        return entropy

    def sample(self, values: List):
        """
        Return a random sample.
        """
        return random.choice(values)

    def weighted_sample(self, values: List,
                        weights: List[float]):
        """
        Return a weighted random sample.
        """
        return random.choices(values, weights=weights, k=1)[0]

    def __repr__(self):
        return "ProbabilisticReasoner()"