"""
pygiga.planning.planner
=======================

Planner module for PyGiga.

Creates and manages execution plans from goals and tasks.
"""

from typing import Any, Dict, List, Optional


class Planner:
    """
    Task planner for PyGiga.
    """

    def __init__(self):
        self._plans: Dict[str, List[Dict[str, Any]]] = {}

    def create_plan(
        self,
        goal: str,
        tasks: List[Dict[str, Any]],
    ) -> None:
        """
        Create a plan for a goal.

        Example
        -------
        tasks = [
            {"name": "Collect Data"},
            {"name": "Train Model"},
            {"name": "Evaluate"}
        ]
        """
        self._plans[goal] = tasks

    def add_task(
        self,
        goal: str,
        task: Dict[str, Any],
    ) -> None:
        """
        Add a task to an existing plan.
        """
        if goal not in self._plans:
            self._plans[goal] = []

        self._plans[goal].append(task)

    def remove_task(
        self,
        goal: str,
        index: int,
    ) -> None:
        """
        Remove a task from a plan.
        """
        if goal not in self._plans:
            raise KeyError(f"Goal '{goal}' not found.")

        del self._plans[goal][index]

    def update_task(
        self,
        goal: str,
        index: int,
        task: Dict[str, Any],
    ) -> None:
        """
        Replace a task.
        """
        if goal not in self._plans:
            raise KeyError(f"Goal '{goal}' not found.")

        self._plans[goal][index] = task

    def get_plan(
        self,
        goal: str,
    ) -> List[Dict[str, Any]]:
        """
        Return the plan for a goal.
        """
        if goal not in self._plans:
            raise KeyError(f"Goal '{goal}' not found.")

        return self._plans[goal]

    def next_task(
        self,
        goal: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Return the next unfinished task.
        """
        if goal not in self._plans:
            return None

        for task in self._plans[goal]:
            if not task.get("completed", False):
                return task

        return None

    def complete_task(
        self,
        goal: str,
        index: int,
    ) -> None:
        """
        Mark a task as completed.
        """
        if goal not in self._plans:
            raise KeyError(f"Goal '{goal}' not found.")

        self._plans[goal][index]["completed"] = True

    def clear_plan(
        self,
        goal: str,
    ) -> None:
        """
        Remove a plan.
        """
        self._plans.pop(goal, None)

    def clear(self) -> None:
        """
        Remove all plans.
        """
        self._plans.clear()

    def goals(self) -> List[str]:
        """
        Return all planned goals.
        """
        return sorted(self._plans.keys())

    def exists(
        self,
        goal: str,
    ) -> bool:
        """
        Check whether a plan exists.
        """
        return goal in self._plans

    def info(self) -> Dict[str, Any]:
        """
        Return planner information.
        """
        return {
            "plans": len(self._plans),
            "goals": self.goals(),
        }

    def __len__(self):
        return len(self._plans)

    def __contains__(self, goal: str):
        return goal in self._plans

    def __repr__(self):
        return (
            f"Planner("
            f"plans={len(self._plans)})"
        )