"""
pygiga.agents.learning_agent
============================

Learning Agent

Responsible for storing experiences and enabling
continuous learning.

Author: PyGiga
"""

from datetime import datetime


class LearningAgent:
    """
    Learning Agent
    """

    def __init__(self):

        self.memory = []

    # --------------------------------------------------
    # Learn
    # --------------------------------------------------

    def learn(
        self,
        perception,
        action,
        reward=None,
        evaluation=None,
    ):
        """
        Store an experience.
        """

        experience = {
            "timestamp": datetime.utcnow().isoformat(),
            "perception": perception,
            "action": action,
            "reward": reward,
            "evaluation": evaluation,
        }

        self.memory.append(experience)

        return experience

    # --------------------------------------------------
    # Experience Replay
    # --------------------------------------------------

    def replay(self):

        """
        Return all stored experiences.
        """

        return self.memory

    # --------------------------------------------------
    # Latest Experience
    # --------------------------------------------------

    def latest(self):

        if not self.memory:
            return None

        return self.memory[-1]

    # --------------------------------------------------
    # Total Experiences
    # --------------------------------------------------

    def count(self):

        return len(self.memory)

    # --------------------------------------------------
    # Clear Memory
    # --------------------------------------------------

    def clear(self):

        self.memory.clear()

    # --------------------------------------------------
    # Reward Statistics
    # --------------------------------------------------

    def average_reward(self):

        rewards = [
            item["reward"]
            for item in self.memory
            if item["reward"] is not None
        ]

        if not rewards:
            return 0

        return sum(rewards) / len(rewards)

    # --------------------------------------------------
    # Search Experiences
    # --------------------------------------------------

    def search(self, keyword):

        results = []

        keyword = keyword.lower()

        for experience in self.memory:

            if keyword in str(experience).lower():
                results.append(experience)

        return results

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def export(self):

        return self.memory

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "experiences": len(self.memory),
            "average_reward": self.average_reward(),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "LearningAgent",
            "status": "ready",
            "experiences": len(self.memory),
        }