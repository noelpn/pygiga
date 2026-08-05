"""
pygiga.learning.scheduler
=========================

Learning Scheduler

Manages learning rate scheduling.

Author: PyGiga
"""

from datetime import datetime


class LearningScheduler:
    """
    Learning Rate Scheduler
    """

    def __init__(self):

        self.initial_learning_rate = 0.001
        self.current_learning_rate = 0.001

        self.step_size = 10
        self.gamma = 0.1

        self.epoch = 0

        self.history = []

    # --------------------------------------------------
    # Configure
    # --------------------------------------------------

    def configure(
        self,
        initial_learning_rate: float = 0.001,
        step_size: int = 10,
        gamma: float = 0.1,
    ):

        self.initial_learning_rate = initial_learning_rate
        self.current_learning_rate = initial_learning_rate

        self.step_size = step_size
        self.gamma = gamma

        self.epoch = 0

        return self.info()

    # --------------------------------------------------
    # Step
    # --------------------------------------------------

    def step(self):

        self.epoch += 1

        if (
            self.step_size > 0
            and self.epoch % self.step_size == 0
        ):

            self.current_learning_rate *= self.gamma

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "epoch": self.epoch,
            "learning_rate": self.current_learning_rate,
        }

        self.history.append(record)

        return record

    # --------------------------------------------------
    # Learning Rate
    # --------------------------------------------------

    def get_learning_rate(self):

        return self.current_learning_rate

    def set_learning_rate(
        self,
        learning_rate: float,
    ):

        self.current_learning_rate = learning_rate

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.current_learning_rate = (
            self.initial_learning_rate
        )

        self.epoch = 0

        self.history.clear()

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def records(self):

        return self.history

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "epochs": self.epoch,
            "learning_rate": self.current_learning_rate,
            "history": len(self.history),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "LearningScheduler",
            "initial_learning_rate": self.initial_learning_rate,
            "current_learning_rate": self.current_learning_rate,
            "step_size": self.step_size,
            "gamma": self.gamma,
            "epoch": self.epoch,
        }