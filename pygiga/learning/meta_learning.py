"""
pygiga.learning.meta_learning
=============================

Meta Learning Module

Provides a simple meta-learning manager.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Any


class MetaLearning:
    """
    Meta Learning Manager

    Learns from previous learning experiences
    to improve future learning.
    """

    def __init__(self):

        self.tasks = []
        self.meta_parameters = {}
        self.history = []

    # --------------------------------------------------
    # Learn Task
    # --------------------------------------------------

    def learn(
        self,
        task_name: str,
        metrics: Dict[str, Any],
    ) -> Dict:
        """
        Record a completed learning task.
        """

        task = {
            "timestamp": datetime.utcnow().isoformat(),
            "task": task_name,
            "metrics": metrics,
        }

        self.tasks.append(task)
        self.history.append(task)

        return task

    # --------------------------------------------------
    # Update Meta Parameters
    # --------------------------------------------------

    def update_parameter(
        self,
        name: str,
        value: Any,
    ):

        self.meta_parameters[name] = value

    # --------------------------------------------------
    # Get Parameter
    # --------------------------------------------------

    def get_parameter(
        self,
        name: str,
        default=None,
    ):

        return self.meta_parameters.get(
            name,
            default,
        )

    # --------------------------------------------------
    # Analyze Learning
    # --------------------------------------------------

    def analyze(self):

        total = len(self.tasks)

        if total == 0:

            return {
                "tasks": 0,
                "average_accuracy": 0,
            }

        accuracies = []

        for task in self.tasks:

            accuracy = task["metrics"].get(
                "accuracy"
            )

            if accuracy is not None:

                accuracies.append(
                    accuracy
                )

        average_accuracy = (
            sum(accuracies) / len(accuracies)
            if accuracies
            else 0
        )

        return {
            "tasks": total,
            "average_accuracy": average_accuracy,
        }

    # --------------------------------------------------
    # Latest Task
    # --------------------------------------------------

    def latest(self):

        if not self.tasks:
            return None

        return self.tasks[-1]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def records(self):

        return self.history

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def clear(self):

        self.tasks.clear()
        self.history.clear()
        self.meta_parameters.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "tasks": len(self.tasks),
            "parameters": len(self.meta_parameters),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "MetaLearning",
            "tasks": len(self.tasks),
            "parameters": len(self.meta_parameters),
        }