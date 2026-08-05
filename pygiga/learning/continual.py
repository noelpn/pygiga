"""
pygiga.learning.continual
=========================

Continual Learning Module

Stores experiences and enables continual learning.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List


class ContinualLearning:
    """
    Continual learning manager.
    """

    def __init__(self):

        self.experiences = []

    # --------------------------------------------------
    # Learn
    # --------------------------------------------------

    def learn(
        self,
        input_data,
        output_data,
        reward=None,
    ):

        experience = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "output": output_data,
            "reward": reward,
        }

        self.experiences.append(
            experience
        )

        return experience

    # --------------------------------------------------
    # Replay
    # --------------------------------------------------

    def replay(self):

        return self.experiences

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.experiences:
            return None

        return self.experiences[-1]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            experience
            for experience in self.experiences
            if keyword in str(experience).lower()
        ]

    # --------------------------------------------------
    # Forget
    # --------------------------------------------------

    def forget_last(self):

        if self.experiences:
            return self.experiences.pop()

        return None

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.experiences.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        rewards = [
            item["reward"]
            for item in self.experiences
            if item["reward"] is not None
        ]

        average_reward = (
            sum(rewards) / len(rewards)
            if rewards
            else 0
        )

        return {
            "experiences": len(
                self.experiences
            ),
            "average_reward": average_reward,
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "ContinualLearning",
            "experiences": len(
                self.experiences
            ),
        }