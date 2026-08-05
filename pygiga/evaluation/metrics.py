"""
pygiga.evaluation.metrics
=========================

Metrics Module

Provides evaluation metrics for PyGiga.

Author: PyGiga
"""

from typing import List, Dict


class Metrics:
    """
    Collect and compute evaluation metrics.
    """

    def __init__(self):

        self.values = {}

    # --------------------------------------------------
    # Add Metric
    # --------------------------------------------------

    def add(
        self,
        name: str,
        value: float,
    ):

        self.values.setdefault(name, [])

        self.values[name].append(value)

    # --------------------------------------------------
    # Get Metric
    # --------------------------------------------------

    def get(
        self,
        name: str,
    ):

        return self.values.get(name, [])

    # --------------------------------------------------
    # Average
    # --------------------------------------------------

    def average(
        self,
        name: str,
    ):

        values = self.get(name)

        if not values:
            return 0

        return sum(values) / len(values)

    # --------------------------------------------------
    # Minimum
    # --------------------------------------------------

    def minimum(
        self,
        name: str,
    ):

        values = self.get(name)

        if not values:
            return 0

        return min(values)

    # --------------------------------------------------
    # Maximum
    # --------------------------------------------------

    def maximum(
        self,
        name: str,
    ):

        values = self.get(name)

        if not values:
            return 0

        return max(values)

    # --------------------------------------------------
    # Total
    # --------------------------------------------------

    def total(
        self,
        name: str,
    ):

        return sum(self.get(name))

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(
        self,
        name: str,
    ):

        return len(self.get(name))

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self) -> Dict:

        report = {}

        for metric in self.values:

            report[metric] = {
                "count": self.count(metric),
                "average": self.average(metric),
                "minimum": self.minimum(metric),
                "maximum": self.maximum(metric),
                "total": self.total(metric),
            }

        return report

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def clear(self):

        self.values.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "metrics": list(self.values.keys()),
            "count": len(self.values),
        }