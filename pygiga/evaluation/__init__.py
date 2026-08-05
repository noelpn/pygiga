"""
pygiga.evaluation
=================

Evaluation Package

Provides benchmarking, metrics, self-reflection,
and reporting utilities for PyGiga.

Author: PyGiga
"""

from .benchmark import Benchmark
from .metrics import Metrics
from .self_reflection import SelfReflection
from .reporting import ReportGenerator

__all__ = [
    "Benchmark",
    "Metrics",
    "SelfReflection",
    "ReportGenerator",
]

__version__ = "0.1.0"