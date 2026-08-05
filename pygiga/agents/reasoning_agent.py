"""
pygiga.agents.reasoning_agent
=============================

Reasoning Agent

Responsible for making decisions from perception
and memory.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class ReasoningAgent:
    """
    PyGiga Reasoning Agent
    """

    def __init__(self):

        self.reasoning_history = []

    # --------------------------------------------------
    # Main Reasoning
    # --------------------------------------------------

    def reason(
        self,
        perception: Dict[str, Any],
        memory: List[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Perform reasoning.
        """

        if memory is None:
            memory = []

        content = perception.get("content", "")

        goal = self.extract_goal(content)

        reasoning = {
            "timestamp": datetime.utcnow().isoformat(),
            "goal": goal,
            "intent": self.detect_intent(content),
            "confidence": self.confidence(content),
            "memory_used": len(memory),
            "decision": self.decision(goal),
        }

        self.reasoning_history.append(reasoning)

        return reasoning

    # --------------------------------------------------
    # Goal Extraction
    # --------------------------------------------------

    def extract_goal(
        self,
        content: Any,
    ) -> str:

        if isinstance(content, str):
            return content.strip()

        return str(content)

    # --------------------------------------------------
    # Intent Detection
    # --------------------------------------------------

    def detect_intent(
        self,
        text: Any,
    ) -> str:

        if not isinstance(text, str):
            return "unknown"

        text = text.lower()

        if "open" in text:
            return "open"

        if "search" in text:
            return "search"

        if "read" in text:
            return "read"

        if "write" in text:
            return "write"

        if "delete" in text:
            return "delete"

        if "send" in text:
            return "send"

        return "general"

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    def confidence(
        self,
        text: Any,
    ) -> float:

        if not text:
            return 0.0

        return 1.0

    # --------------------------------------------------
    # Decision
    # --------------------------------------------------

    def decision(
        self,
        goal: str,
    ) -> str:

        return f"Proceed with: {goal}"

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.reasoning_history:
            return None

        return self.reasoning_history[-1]

    def history(self):

        return self.reasoning_history

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ):

        keyword = keyword.lower()

        return [
            item
            for item in self.reasoning_history
            if keyword in str(item).lower()
        ]

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.reasoning_history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "reasoning_operations": len(
                self.reasoning_history
            )
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "ReasoningAgent",
            "status": "ready",
            "history": len(
                self.reasoning_history
            ),
        }