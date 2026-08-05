"""
pygiga.datasets
===============

Dataset Management Package

Provides dataset loading, preprocessing,
augmentation and streaming.

Author: PyGiga
"""

from .loader import DatasetLoader
from .preprocessing import DatasetPreprocessor
from .augmentation import DatasetAugmentation
from .streaming import DatasetStreamer

__all__ = [
    "DatasetLoader",
    "DatasetPreprocessor",
    "DatasetAugmentation",
    "DatasetStreamer",
]

__version__ = "0.1.0"