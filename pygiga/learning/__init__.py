"""
pygiga.learning
===============

Learning Package

Provides learning algorithms for PyGiga.

Author: PyGiga
"""

from .adaptation import AdaptationManager
from .continual import ContinualLearning
from .reinforcement import ReinforcementLearning
from .supervised import SupervisedLearning
from .unsupervised import UnsupervisedLearning
from .self_supervised import SelfSupervisedLearning
from .meta_learning import MetaLearning
from .online import OnlineLearning
from .trainer import Trainer
from .optimizer import Optimizer
from .scheduler import LearningScheduler

__all__ = [
    "AdaptationManager",
    "ContinualLearning",
    "ReinforcementLearning",
    "SupervisedLearning",
    "UnsupervisedLearning",
    "SelfSupervisedLearning",
    "MetaLearning",
    "OnlineLearning",
    "Trainer",
    "Optimizer",
    "LearningScheduler",
]

__version__ = "0.1.0"