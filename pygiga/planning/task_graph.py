"""
pygiga.planning.task_graph
==========================

Task graph for PyGiga.

Represents task dependencies as a directed graph and
provides traversal utilities.
"""

from collections import deque
from typing import Dict, List, Set


class TaskGraph:
    """
    Directed acyclic task graph (DAG).
    """

    def __init__(self):
        self._graph: Dict[str, Set[str]] = {}
        self._reverse: Dict[str, Set[str]] = {}

    def add_task(self, name: str) -> None:
        """
        Add a task node.
        """
        self._graph.setdefault(name, set())
        self._reverse.setdefault(name, set())

    def remove_task(self, name: str) -> None:
        """
        Remove a task and its dependencies.
        """
        if name not in self._graph:
            return

        for dependency in self._reverse[name]:
            self._graph[dependency].discard(name)

        for child in self._graph[name]:
            self._reverse[child].discard(name)

        del self._graph[name]
        del self._reverse[name]

    def add_dependency(
        self,
        task: str,
        depends_on: str,
    ) -> None:
        """
        task depends_on dependency.

        dependency ---> task
        """
        self.add_task(task)
        self.add_task(depends_on)

        self._graph[depends_on].add(task)
        self._reverse[task].add(depends_on)

    def remove_dependency(
        self,
        task: str,
        depends_on: str,
    ) -> None:
        """
        Remove a dependency.
        """
        if depends_on in self._graph:
            self._graph[depends_on].discard(task)

        if task in self._reverse:
            self._reverse[task].discard(depends_on)

    def dependencies(
        self,
        task: str,
    ) -> List[str]:
        """
        Return task dependencies.
        """
        return sorted(
            self._reverse.get(task, [])
        )

    def dependents(
        self,
        task: str,
    ) -> List[str]:
        """
        Return tasks depending on task.
        """
        return sorted(
            self._graph.get(task, [])
        )

    def execution_order(self) -> List[str]:
        """
        Topological ordering.
        """
        indegree = {
            node: len(deps)
            for node, deps in self._reverse.items()
        }

        queue = deque(
            [
                node
                for node, degree in indegree.items()
                if degree == 0
            ]
        )

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for child in self._graph[node]:
                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)

        if len(order) != len(self._graph):
            raise RuntimeError(
                "Cycle detected in task graph."
            )

        return order

    def has_cycle(self) -> bool:
        """
        Check whether the graph contains a cycle.
        """
        try:
            self.execution_order()
            return False
        except RuntimeError:
            return True

    def exists(
        self,
        task: str,
    ) -> bool:
        """
        Check whether a task exists.
        """
        return task in self._graph

    def tasks(self) -> List[str]:
        """
        Return all tasks.
        """
        return sorted(self._graph.keys())

    def clear(self) -> None:
        """
        Remove all tasks.
        """
        self._graph.clear()
        self._reverse.clear()

    def info(self):
        """
        Return graph information.
        """
        edges = sum(
            len(children)
            for children in self._graph.values()
        )

        return {
            "tasks": len(self._graph),
            "dependencies": edges,
            "has_cycle": self.has_cycle(),
        }

    def __len__(self):
        return len(self._graph)

    def __contains__(self, task: str):
        return task in self._graph

    def __repr__(self):
        return (
            f"TaskGraph("
            f"tasks={len(self._graph)})"
        )