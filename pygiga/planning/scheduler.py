"""
pygiga.planning.scheduler
=========================

Task scheduler for PyGiga.

Provides scheduling, prioritization, and queue
management for planned tasks.
"""

from heapq import heappop, heappush
from typing import Any, Dict, List, Optional


class Scheduler:
    """
    Priority-based task scheduler.
    """

    def __init__(self):
        self._queue: List = []

    def schedule(
        self,
        name: str,
        priority: int = 1,
        data: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Schedule a task.

        Lower priority values execute first.

        Example
        -------
        scheduler.schedule(
            "Train Model",
            priority=1
        )
        """
        heappush(
            self._queue,
            (
                priority,
                name,
                data or {},
            ),
        )

    def next_task(self) -> Optional[Dict[str, Any]]:
        """
        Return the next scheduled task
        without removing it.
        """
        if not self._queue:
            return None

        priority, name, data = self._queue[0]

        return {
            "name": name,
            "priority": priority,
            "data": data,
        }

    def pop_task(self) -> Optional[Dict[str, Any]]:
        """
        Remove and return the next task.
        """
        if not self._queue:
            return None

        priority, name, data = heappop(
            self._queue
        )

        return {
            "name": name,
            "priority": priority,
            "data": data,
        }

    def clear(self) -> None:
        """
        Remove all scheduled tasks.
        """
        self._queue.clear()

    def is_empty(self) -> bool:
        """
        Check whether the scheduler
        contains tasks.
        """
        return len(self._queue) == 0

    def tasks(self) -> List[Dict[str, Any]]:
        """
        Return all scheduled tasks.
        """
        return [
            {
                "name": name,
                "priority": priority,
                "data": data,
            }
            for priority, name, data in sorted(
                self._queue
            )
        ]

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a task exists.
        """
        return any(
            task_name == name
            for _, task_name, _ in self._queue
        )

    def remove(
        self,
        name: str,
    ) -> bool:
        """
        Remove a scheduled task.
        """
        for index, (_, task_name, _) in enumerate(
            self._queue
        ):
            if task_name == name:
                del self._queue[index]
                self._queue.sort()
                return True

        return False

    def info(self) -> Dict[str, Any]:
        """
        Return scheduler information.
        """
        return {
            "scheduled_tasks": len(self._queue),
            "empty": self.is_empty(),
        }

    def __len__(self):
        return len(self._queue)

    def __contains__(self, name: str):
        return self.exists(name)

    def __repr__(self):
        return (
            f"Scheduler("
            f"tasks={len(self._queue)})"
        )