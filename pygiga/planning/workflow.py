"""
pygiga.planning.workflow
========================

Workflow manager for PyGiga.

Provides workflow creation, execution,
tracking, and management.
"""

from typing import Any, Callable, Dict, List, Optional


class Workflow:
    """
    Workflow execution manager.
    """

    def __init__(self):
        self._workflows: Dict[str, List[Dict[str, Any]]] = {}

    def create(
        self,
        name: str,
        steps: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        """
        Create a workflow.
        """
        self._workflows[name] = steps or []

    def delete(
        self,
        name: str,
    ) -> None:
        """
        Delete a workflow.
        """
        self._workflows.pop(name, None)

    def add_step(
        self,
        workflow: str,
        name: str,
        action: Callable,
        *args,
        **kwargs,
    ) -> None:
        """
        Add a step to a workflow.
        """
        if workflow not in self._workflows:
            self.create(workflow)

        self._workflows[workflow].append(
            {
                "name": name,
                "action": action,
                "args": args,
                "kwargs": kwargs,
            }
        )

    def remove_step(
        self,
        workflow: str,
        index: int,
    ) -> None:
        """
        Remove a workflow step.
        """
        if workflow not in self._workflows:
            raise KeyError(
                f"Workflow '{workflow}' not found."
            )

        del self._workflows[workflow][index]

    def execute(
        self,
        workflow: str,
    ) -> List[Any]:
        """
        Execute every step in a workflow.
        """
        if workflow not in self._workflows:
            raise KeyError(
                f"Workflow '{workflow}' not found."
            )

        results = []

        for step in self._workflows[workflow]:
            result = step["action"](
                *step["args"],
                **step["kwargs"],
            )

            results.append(
                {
                    "step": step["name"],
                    "result": result,
                }
            )

        return results

    def get(
        self,
        workflow: str,
    ) -> List[Dict[str, Any]]:
        """
        Return a workflow.
        """
        if workflow not in self._workflows:
            raise KeyError(
                f"Workflow '{workflow}' not found."
            )

        return self._workflows[workflow]

    def workflows(self) -> List[str]:
        """
        Return all workflow names.
        """
        return sorted(self._workflows.keys())

    def exists(
        self,
        workflow: str,
    ) -> bool:
        """
        Check whether a workflow exists.
        """
        return workflow in self._workflows

    def clear(self) -> None:
        """
        Remove all workflows.
        """
        self._workflows.clear()

    def info(self) -> Dict[str, Any]:
        """
        Return workflow information.
        """
        return {
            "workflows": len(self._workflows),
            "names": self.workflows(),
        }

    def __len__(self):
        return len(self._workflows)

    def __contains__(self, workflow: str):
        return workflow in self._workflows

    def __repr__(self):
        return (
            f"Workflow("
            f"count={len(self._workflows)})"
        )