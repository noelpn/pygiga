"""
pygiga.learning.supervised
==========================

Supervised Learning Module

Provides supervised learning utilities.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class SupervisedLearning:
    """
    Supervised Learning Manager

    Manages labeled training samples.
    """

    def __init__(self):

        self.dataset = []
        self.labels = set()
        self.history = []

    # --------------------------------------------------
    # Add Sample
    # --------------------------------------------------

    def learn(
        self,
        input_data: Any,
        label: Any,
    ) -> Dict:
        """
        Add a labeled training sample.
        """

        sample = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "label": label,
        }

        self.dataset.append(sample)
        self.labels.add(label)
        self.history.append(sample)

        return sample

    # --------------------------------------------------
    # Dataset
    # --------------------------------------------------

    def dataset_size(self) -> int:

        return len(self.dataset)

    def get_dataset(self) -> List[Dict]:

        return self.dataset

    # --------------------------------------------------
    # Labels
    # --------------------------------------------------

    def get_labels(self):

        return sorted(self.labels)

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            sample
            for sample in self.dataset
            if keyword in str(sample).lower()
        ]

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.dataset:
            return None

        return self.dataset[-1]

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def forget_last(self):

        if self.dataset:

            sample = self.dataset.pop()

            self.history.pop()

            return sample

        return None

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def clear(self):

        self.dataset.clear()
        self.labels.clear()
        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "samples": len(self.dataset),
            "classes": len(self.labels),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "SupervisedLearning",
            "samples": len(self.dataset),
            "classes": len(self.labels),
        }