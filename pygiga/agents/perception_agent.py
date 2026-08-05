"""
pygiga.agents.perception_agent
==============================

Perception Agent

Responsible for receiving and preprocessing input.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict


class PerceptionAgent:
    """
    Perception Agent
    """

    def __init__(self):

        self.history = []

    # --------------------------------------------------
    # Main Processing
    # --------------------------------------------------

    def process(self, data: Any) -> Dict:
        """
        Process incoming data.
        """

        perception = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": self.detect_type(data),
            "content": data,
            "length": self.length(data),
        }

        self.history.append(perception)

        return perception

    # --------------------------------------------------
    # Detect Input Type
    # --------------------------------------------------

    def detect_type(self, data: Any) -> str:

        if isinstance(data, str):
            return "text"

        if isinstance(data, bytes):
            return "binary"

        if isinstance(data, dict):
            return "structured"

        if isinstance(data, list):
            return "sequence"

        if isinstance(data, (int, float)):
            return "number"

        return "unknown"

    # --------------------------------------------------
    # Length
    # --------------------------------------------------

    def length(self, data: Any) -> int:

        try:
            return len(data)

        except Exception:
            return 1

    # --------------------------------------------------
    # Normalize Text
    # --------------------------------------------------

    def normalize(self, text: str) -> str:

        return text.strip().lower()

    # --------------------------------------------------
    # Tokenize
    # --------------------------------------------------

    def tokenize(self, text: str):

        return text.split()

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def all(self):

        return self.history

    def clear(self):

        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "processed_inputs": len(self.history)
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "PerceptionAgent",
            "status": "ready",
            "processed": len(self.history),
        }