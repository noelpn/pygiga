"""
pygiga.learning.optimizer
=========================

Optimizer Module

Provides optimizer management for PyGiga.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, Any


class Optimizer:
    """
    Optimizer Manager

    Stores optimization parameters and
    optimization history.
    """

    def __init__(self):

        self.name = "SGD"
        self.learning_rate = 0.001
        self.weight_decay = 0.0
        self.momentum = 0.0

        self.history = []

    # --------------------------------------------------
    # Configure
    # --------------------------------------------------

    def configure(
        self,
        name: str = "SGD",
        learning_rate: float = 0.001,
        weight_decay: float = 0.0,
        momentum: float = 0.0,
    ):

        self.name = name
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.momentum = momentum

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "optimizer": self.name,
            "learning_rate": self.learning_rate,
            "weight_decay": self.weight_decay,
            "momentum": self.momentum,
        }

        self.history.append(record)

        return record

    # --------------------------------------------------
    # Learning Rate
    # --------------------------------------------------

    def set_learning_rate(
        self,
        learning_rate: float,
    ):

        self.learning_rate = learning_rate

    def get_learning_rate(self):

        return self.learning_rate

    # --------------------------------------------------
    # Optimizer Name
    # --------------------------------------------------

    def set_optimizer(
        self,
        name: str,
    ):

        self.name = name

    def get_optimizer(self):

        return self.name

    # --------------------------------------------------
    # Simulate Optimization Step
    # --------------------------------------------------

    def step(self):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "optimizer": self.name,
            "learning_rate": self.learning_rate,
            "status": "step_completed",
        }

        self.history.append(record)

        return record

    # --------------------------------------------------
    # Zero Grad
    # --------------------------------------------------

    def zero_grad(self):

        return {
            "status": "gradients_cleared"
        }

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def records(self):

        return self.history

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "optimizer": self.name,
            "learning_rate": self.learning_rate,
            "optimization_steps": len(self.history),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "Optimizer",
            "optimizer": self.name,
            "learning_rate": self.learning_rate,
        }