"""
pygiga.agents.planning_agent
============================

Planning Agent

Responsible for creating execution plans.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Any


class PlanningAgent:
    """
    Planning Agent
    """

    def __init__(self):

        self.plan_history = []

    # --------------------------------------------------
    # Create Plan
    # --------------------------------------------------

    def plan(self, reasoning: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create an execution plan from reasoning.
        """

        goal = reasoning.get("goal", "Unknown Goal")

        plan = {
            "timestamp": datetime.utcnow().isoformat(),
            "goal": goal,
            "steps": self.generate_steps(goal),
            "status": "planned",
        }

        self.plan_history.append(plan)

        return plan

    # --------------------------------------------------
    # Generate Steps
    # --------------------------------------------------

    def generate_steps(self, goal: str) -> List[Dict[str, Any]]:
        """
        Generate execution steps.

        (Simple placeholder implementation)
        """

        return [
            {
                "step": 1,
                "action": "analyze",
                "description": goal,
            },
            {
                "step": 2,
                "action": "execute",
                "description": goal,
            },
            {
                "step": 3,
                "action": "verify",
                "description": "Verify execution result",
            },
        ]

    # --------------------------------------------------
    # Add Step
    # --------------------------------------------------

    def add_step(
        self,
        plan: Dict[str, Any],
        action: str,
        description: str,
    ) -> Dict[str, Any]:

        step_number = len(plan["steps"]) + 1

        plan["steps"].append(
            {
                "step": step_number,
                "action": action,
                "description": description,
            }
        )

        return plan

    # --------------------------------------------------
    # Remove Step
    # --------------------------------------------------

    def remove_step(
        self,
        plan: Dict[str, Any],
        step_number: int,
    ) -> Dict[str, Any]:

        plan["steps"] = [
            step
            for step in plan["steps"]
            if step["step"] != step_number
        ]

        return plan

    # --------------------------------------------------
    # Latest Plan
    # --------------------------------------------------

    def latest(self):

        if not self.plan_history:
            return None

        return self.plan_history[-1]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def history(self):

        return self.plan_history

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.plan_history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "plans_created": len(self.plan_history)
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "PlanningAgent",
            "status": "ready",
            "plans": len(self.plan_history),
        }