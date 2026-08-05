"""
pygiga.memory.episodic
======================

Episodic Memory

Stores experiences and events.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class EpisodicMemory:
    """
    Episodic Memory
    """

    def __init__(self):

        self.episodes = []

    # --------------------------------------------------
    # Store Episode
    # --------------------------------------------------

    def remember(
        self,
        event: str,
        data: Any = None,
    ) -> Dict:

        episode = {
            "id": len(self.episodes) + 1,
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "data": data,
        }

        self.episodes.append(episode)

        return episode

    # --------------------------------------------------
    # Recall
    # --------------------------------------------------

    def recall(self):

        return self.episodes

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.episodes:
            return None

        return self.episodes[-1]

    # --------------------------------------------------
    # Get by ID
    # --------------------------------------------------

    def get(
        self,
        episode_id: int,
    ):

        for episode in self.episodes:

            if episode["id"] == episode_id:
                return episode

        return None

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            episode
            for episode in self.episodes
            if keyword in str(episode).lower()
        ]

    # --------------------------------------------------
    # Forget Last
    # --------------------------------------------------

    def forget_last(self):

        if self.episodes:
            return self.episodes.pop()

        return None

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.episodes.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "episodes": len(self.episodes),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "EpisodicMemory",
            "episodes": len(self.episodes),
        }