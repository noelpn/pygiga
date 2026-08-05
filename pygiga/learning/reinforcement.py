"""
pygiga.learning.reinforcement
=============================

Reinforcement Learning Module

Provides a simple reinforcement learning manager.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class ReinforcementLearning:
    """
    Reinforcement Learning Manager
    """

    def __init__(self):

        self.experiences = []
        self.total_reward = 0.0
        self.episodes = 0

    # --------------------------------------------------
    # Learn
    # --------------------------------------------------

    def learn(
        self,
        state: Any,
        action: Any,
        reward: float,
        next_state: Any,
        done: bool = False,
    ) -> Dict:
        """
        Store a reinforcement learning experience.
        """

        experience = {
            "timestamp": datetime.utcnow().isoformat(),
            "state": state,
            "action": action,
            "reward": reward,
            "next_state": next_state,
            "done": done,
        }

        self.experiences.append(experience)

        self.total_reward += reward

        if done:
            self.episodes += 1

        return experience

    # --------------------------------------------------
    # Experience Replay
    # --------------------------------------------------

    def replay(self) -> List[Dict]:

        return self.experiences

    # --------------------------------------------------
    # Latest Experience
    # --------------------------------------------------

    def latest(self):

        if not self.experiences:
            return None

        return self.experiences[-1]

    # --------------------------------------------------
    # Episode Reward
    # --------------------------------------------------

    def average_reward(self) -> float:

        if self.episodes == 0:
            return self.total_reward

        return self.total_reward / self.episodes

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            item
            for item in self.experiences
            if keyword in str(item).lower()
        ]

    # --------------------------------------------------
    # Remove Last
    # --------------------------------------------------

    def forget_last(self):

        if self.experiences:

            last = self.experiences.pop()

            self.total_reward -= last["reward"]

            return last

        return None

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.experiences.clear()
        self.total_reward = 0.0
        self.episodes = 0

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "experiences": len(self.experiences),
            "episodes": self.episodes,
            "total_reward": self.total_reward,
            "average_reward": self.average_reward(),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "ReinforcementLearning",
            "experiences": len(self.experiences),
            "episodes": self.episodes,
        }