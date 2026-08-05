"""
pygiga.planning.execution
=========================

Execution engine for PyGiga.

Responsible for executing plans, workflows,
tasks, and callable actions.
"""

from typing import Any, Callable, Dict, List


class ExecutionEngine:
    """
    Executes registered actions and task sequences.
    """

    def __init__(self):
        self._actions: Dict[str, Callable] = {}
        self.history: List[Dict[str, Any]] = []

    def register_action(
        self,
        name: str,
        action: Callable,
    ) -> None:
        """
        Register an executable action.
        """
        if not callable(action):
            raise TypeError("Action must be callable.")

        self._actions[name] = action

    def unregister_action(
        self,
        name: str,
    ) -> None:
        """
        Remove an action.
        """
        self._actions.pop(name, None)

    def execute(
        self,
        name: str,
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute a registered action.
        """
        if name not in self._actions:
            raise KeyError(
                f"Action '{name}' is not registered."
            )

        result = self._actions[name](*args, **kwargs)

        self.history.append(
            {
                "action": name,
                "args": args,
                "kwargs": kwargs,
                "result": result,
            }
        )

        return result

    def execute_plan(
        self,
        plan: List[Dict[str, Any]],
    ) -> List[Any]:
        """
        Execute a sequence of tasks.

        Example
        -------
        [
            {"action": "step1"},
            {"action": "step2", "args": [10]}
        ]
        """
        results = []

        for step in plan:
            action = step["action"]
            args = step.get("args", [])
            kwargs = step.get("kwargs", {})

            results.append(
                self.execute(
                    action,
                    *args,
                    **kwargs,
                )
            )

        return results

    def clear_history(self) -> None:
        """
        Clear execution history.
        """
        self.history.clear()

    def actions(self) -> List[str]:
        """
        Return registered actions.
        """
        return sorted(self._actions.keys())

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check if an action exists.
        """
        return name in self._actions

    def info(self) -> Dict[str, Any]:
        """
        Return execution engine information.
        """
        return {
            "registered_actions": len(self._actions),
            "history_length": len(self.history),
            "actions": self.actions(),
        }

    def __len__(self):
        return len(self._actions)

    def __contains__(self, name: str):
        return name in self._actions

    def __repr__(self):
        return (
            f"ExecutionEngine("
            f"actions={len(self._actions)})"
        )