"""
pygiga.planning.goal_manager
============================

Goal manager for PyGiga.

Provides goal creation, tracking, prioritization,
completion, and removal.
"""

from typing import Any, Dict, List, Optional


class GoalManager:
    """
    Manages goals for planning systems.
    """

    def __init__(self):
        self._goals: Dict[str, Dict[str, Any]] = {}

    def add_goal(
        self,
        name: str,
        description: str = "",
        priority: int = 1,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Add a new goal.
        """
        self._goals[name] = {
            "description": description,
            "priority": priority,
            "completed": False,
            "metadata": metadata or {},
        }

    def remove_goal(
        self,
        name: str,
    ) -> None:
        """
        Remove a goal.
        """
        self._goals.pop(name, None)

    def complete_goal(
        self,
        name: str,
    ) -> None:
        """
        Mark a goal as completed.
        """
        if name not in self._goals:
            raise KeyError(f"Goal '{name}' not found.")

        self._goals[name]["completed"] = True

    def reopen_goal(
        self,
        name: str,
    ) -> None:
        """
        Reopen a completed goal.
        """
        if name not in self._goals:
            raise KeyError(f"Goal '{name}' not found.")

        self._goals[name]["completed"] = False

    def get_goal(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """
        Return a goal.
        """
        if name not in self._goals:
            raise KeyError(f"Goal '{name}' not found.")

        return self._goals[name]

    def list_goals(
        self,
        completed: Optional[bool] = None,
    ) -> List[str]:
        """
        List goals.

        completed=None -> all
        completed=True -> completed only
        completed=False -> active only
        """
        if completed is None:
            return list(self._goals.keys())

        return [
            goal
            for goal, info in self._goals.items()
            if info["completed"] == completed
        ]

    def prioritize(self) -> List[str]:
        """
        Return goals sorted by priority.
        """
        return [
            goal
            for goal, _ in sorted(
                self._goals.items(),
                key=lambda item: item[1]["priority"],
                reverse=True,
            )
        ]

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a goal exists.
        """
        return name in self._goals

    def clear(self) -> None:
        """
        Remove all goals.
        """
        self._goals.clear()

    def info(self) -> Dict[str, Any]:
        """
        Return goal manager information.
        """
        return {
            "total_goals": len(self._goals),
            "completed": len(self.list_goals(True)),
            "active": len(self.list_goals(False)),
        }

    def __len__(self):
        return len(self._goals)

    def __contains__(self, name: str):
        return name in self._goals

    def __repr__(self):
        return (
            f"GoalManager("
            f"goals={len(self._goals)})"
        )