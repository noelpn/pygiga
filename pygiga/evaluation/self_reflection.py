"""
pygiga.evaluation.self_reflection
================================

Self Reflection Module

Allows PyGiga to analyze its own performance.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Any


class SelfReflection:
    """
    Self-reflection system for PyGiga.
    """

    def __init__(self):

        self.reflections = []

    # --------------------------------------------------
    # Reflect
    # --------------------------------------------------

    def reflect(
        self,
        perception: Any = None,
        reasoning: Any = None,
        plan: Any = None,
        action: Any = None,
        evaluation: Any = None,
    ) -> Dict:
        """
        Create a reflection about the latest task.
        """

        reflection = {
            "timestamp": datetime.utcnow().isoformat(),
            "perception": perception,
            "reasoning": reasoning,
            "plan": plan,
            "action": action,
            "evaluation": evaluation,
            "improvements": self.suggest_improvements(
                evaluation
            ),
        }

        self.reflections.append(reflection)

        return reflection

    # --------------------------------------------------
    # Improvement Suggestions
    # --------------------------------------------------

    def suggest_improvements(
        self,
        evaluation: Any,
    ) -> List[str]:

        suggestions = []

        if evaluation is None:

            suggestions.append(
                "No evaluation available."
            )

            return suggestions

        if isinstance(evaluation, dict):

            if not evaluation.get("success", True):

                suggestions.append(
                    "Improve reasoning before planning."
                )

                suggestions.append(
                    "Review execution strategy."
                )

            score = evaluation.get("score")

            if score is not None and score < 80:

                suggestions.append(
                    "Increase confidence before execution."
                )

        if not suggestions:

            suggestions.append(
                "Performance is satisfactory."
            )

        return suggestions

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.reflections:
            return None

        return self.reflections[-1]

    def history(self):

        return self.reflections

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "reflections": len(self.reflections)
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.reflections.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "SelfReflection",
            "stored_reflections": len(
                self.reflections
            ),
        }