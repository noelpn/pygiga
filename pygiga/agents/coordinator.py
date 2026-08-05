"""
pygiga.agents.coordinator
=========================

Agent Coordinator

Coordinates all cognitive agents.

Author: PyGiga
"""

from .communication import AgentCommunication
from .perception_agent import PerceptionAgent
from .memory_agent import MemoryAgent
from .reasoning_agent import ReasoningAgent
from .planning_agent import PlanningAgent
from .learning_agent import LearningAgent
from .action_agent import ActionAgent
from .evaluator_agent import EvaluatorAgent


class AgentCoordinator:
    """
    Coordinates all PyGiga agents.
    """

    def __init__(self):

        self.communication = AgentCommunication()

        self.perception = PerceptionAgent()
        self.memory = MemoryAgent()
        self.reasoning = ReasoningAgent()
        self.planning = PlanningAgent()
        self.action = ActionAgent()
        self.learning = LearningAgent()
        self.evaluator = EvaluatorAgent()

    # --------------------------------------------------
    # Run Cognitive Pipeline
    # --------------------------------------------------

    def run(self, user_input):

        # 1. Perception
        perception = self.perception.process(user_input)

        self.communication.send(
            "PerceptionAgent",
            "MemoryAgent",
            perception,
        )

        # 2. Memory

        self.memory.store(perception)

        memory = self.memory.retrieve()

        self.communication.send(
            "MemoryAgent",
            "ReasoningAgent",
            memory,
        )

        # 3. Reasoning

        reasoning = self.reasoning.reason(
            perception,
            memory,
        )

        self.communication.send(
            "ReasoningAgent",
            "PlanningAgent",
            reasoning,
        )

        # 4. Planning

        plan = self.planning.plan(reasoning)

        self.communication.send(
            "PlanningAgent",
            "ActionAgent",
            plan,
        )

        # 5. Execute

        action = self.action.execute(plan)

        self.communication.send(
            "ActionAgent",
            "LearningAgent",
            action,
        )

        # 6. Learn

        self.learning.learn(
            perception,
            action,
        )

        # 7. Evaluate

        evaluation = self.evaluator.evaluate(
            perception,
            reasoning,
            plan,
            action,
        )

        return {
            "perception": perception,
            "memory": memory,
            "reasoning": reasoning,
            "plan": plan,
            "action": action,
            "evaluation": evaluation,
        }

    # --------------------------------------------------
    # Individual Access
    # --------------------------------------------------

    def perception_agent(self):
        return self.perception

    def memory_agent(self):
        return self.memory

    def reasoning_agent(self):
        return self.reasoning

    def planning_agent(self):
        return self.planning

    def action_agent(self):
        return self.action

    def learning_agent(self):
        return self.learning

    def evaluator_agent(self):
        return self.evaluator

    # --------------------------------------------------
    # Communication
    # --------------------------------------------------

    def messages(self):

        return self.communication.history()

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def status(self):

        return {
            "coordinator": "running",
            "agents": [
                "PerceptionAgent",
                "MemoryAgent",
                "ReasoningAgent",
                "PlanningAgent",
                "ActionAgent",
                "LearningAgent",
                "EvaluatorAgent",
            ],
            "messages": len(
                self.communication.history()
            ),
        }