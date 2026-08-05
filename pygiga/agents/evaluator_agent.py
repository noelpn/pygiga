"""
pygiga.agents.evaluator_agent
=============================

Evaluator Agent

Evaluates the quality of the cognitive pipeline.

Author: PyGiga
"""

from datetime import datetime


class EvaluatorAgent:
    """
    Evaluates plans and execution results.
    """

    def __init__(self):

        self.history = []

    # --------------------------------------------------
    # Main Evaluation
    # --------------------------------------------------

    def evaluate(
        self,
        perception,
        reasoning,
        plan,
        action,
    ):
        """
        Evaluate the execution.
        """

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "success": self._success(action),
            "score": self._score(action),
            "feedback": self._feedback(action),
            "perception": perception,
            "reasoning": reasoning,
            "plan": plan,
            "action": action,
        }

        self.history.append(report)

        return report

    # --------------------------------------------------
    # Success
    # --------------------------------------------------

    def _success(self, action):

        if isinstance(action, dict):
            return action.get("status") == "success"

        return False

    # --------------------------------------------------
    # Score
    # --------------------------------------------------

    def _score(self, action):

        if self._success(action):
            return 100

        return 0

    # --------------------------------------------------
    # Feedback
    # --------------------------------------------------

    def _feedback(self, action):

        if self._success(action):
            return "Task completed successfully."

        return "Task execution failed."

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def evaluations(self):

        return self.history

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def clear(self):

        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        total = len(self.history)

        successful = sum(
            1
            for item in self.history
            if item["success"]
        )

        failed = total - successful

        success_rate = (
            (successful / total) * 100
            if total
            else 0
        )

        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "success_rate": success_rate,
        }

    # --------------------------------------------------
    # Agent Info
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "EvaluatorAgent",
            "history": len(self.history),
        }