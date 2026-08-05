"""
pygiga.learning.online
======================

Online Learning Module

Learns continuously from streaming data.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class OnlineLearning:
    """
    Online Learning Manager

    Continuously updates knowledge from
    incoming data streams.
    """

    def __init__(self):

        self.samples = []
        self.model_state = {}
        self.total_updates = 0

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(
        self,
        input_data: Any,
        target: Any = None,
        prediction: Any = None,
    ) -> Dict:
        """
        Process one online learning sample.
        """

        sample = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "target": target,
            "prediction": prediction,
        }

        self.samples.append(sample)

        self.total_updates += 1

        return sample

    # --------------------------------------------------
    # Update Model State
    # --------------------------------------------------

    def set_state(
        self,
        key: str,
        value: Any,
    ):

        self.model_state[key] = value

    # --------------------------------------------------
    # Get Model State
    # --------------------------------------------------

    def get_state(
        self,
        key: str,
        default=None,
    ):

        return self.model_state.get(
            key,
            default,
        )

    # --------------------------------------------------
    # Latest Sample
    # --------------------------------------------------

    def latest(self):

        if not self.samples:
            return None

        return self.samples[-1]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def history(self):

        return self.samples

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
            for sample in self.samples
            if keyword in str(sample).lower()
        ]

    # --------------------------------------------------
    # Remove Last
    # --------------------------------------------------

    def forget_last(self):

        if self.samples:

            self.total_updates -= 1

            return self.samples.pop()

        return None

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def clear(self):

        self.samples.clear()
        self.model_state.clear()
        self.total_updates = 0

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "updates": self.total_updates,
            "samples": len(self.samples),
            "state_variables": len(
                self.model_state
            ),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "OnlineLearning",
            "updates": self.total_updates,
            "samples": len(self.samples),
        }