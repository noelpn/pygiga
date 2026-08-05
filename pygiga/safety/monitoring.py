"""
pygiga.safety.monitoring
========================

Safety Monitoring Module

Provides runtime monitoring utilities for detecting
warnings, errors, and safety-related events.
"""

from datetime import datetime
from typing import Dict, List


class SafetyMonitor:
    """
    Basic runtime safety monitor.
    """

    def __init__(self):
        self._events: List[Dict] = []

    def log(
        self,
        level: str,
        message: str,
        source: str = "system",
    ) -> None:
        """
        Record a safety event.
        """
        self._events.append(
            {
                "time": datetime.utcnow(),
                "level": level.upper(),
                "source": source,
                "message": message,
            }
        )

    def info(self, message: str, source: str = "system") -> None:
        """
        Record an informational event.
        """
        self.log("INFO", message, source)

    def warning(self, message: str, source: str = "system") -> None:
        """
        Record a warning event.
        """
        self.log("WARNING", message, source)

    def error(self, message: str, source: str = "system") -> None:
        """
        Record an error event.
        """
        self.log("ERROR", message, source)

    def events(self) -> List[Dict]:
        """
        Return all recorded events.
        """
        return list(self._events)

    def latest(self):
        """
        Return the latest recorded event.
        """
        if not self._events:
            return None
        return self._events[-1]

    def clear(self):
        """
        Remove all recorded events.
        """
        self._events.clear()

    def __len__(self):
        return len(self._events)

    def __repr__(self):
        return f"SafetyMonitor(events={len(self._events)})"