"""
pygiga.learning.adaptation
==========================

Adaptation Module

Responsible for adapting system parameters
based on experience.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, Any


class AdaptationManager:
    """
    Manages adaptive parameters.
    """

    def __init__(self):

        self.parameters = {}
        self.history = []

    # --------------------------------------------------
    # Set Parameter
    # --------------------------------------------------

    def set_parameter(
        self,
        name: str,
        value: Any,
    ):

        self.parameters[name] = value

    # --------------------------------------------------
    # Get Parameter
    # --------------------------------------------------

    def get_parameter(
        self,
        name: str,
        default=None,
    ):

        return self.parameters.get(
            name,
            default,
        )

    # --------------------------------------------------
    # Adapt
    # --------------------------------------------------

    def adapt(
        self,
        feedback: Dict,
    ):

        success = feedback.get(
            "success",
            False,
        )

        confidence = self.parameters.get(
            "confidence",
            0.5,
        )

        if success:

            confidence = min(
                confidence + 0.05,
                1.0,
            )

        else:

            confidence = max(
                confidence - 0.05,
                0.0,
            )

        self.parameters["confidence"] = confidence

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "feedback": feedback,
            "confidence": confidence,
        }

        self.history.append(record)

        return record

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.parameters.clear()
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
            "adaptations": len(self.history),
            "parameters": len(self.parameters),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "AdaptationManager",
            "parameters": len(self.parameters),
        }