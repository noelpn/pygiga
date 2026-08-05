"""
pygiga.agents
=============

Agent System for PyGiga

This package contains the various cognitive agents used by
PyGiga.

Author: PyGiga
"""

from .coordinator import AgentCoordinator
from .communication import AgentCommunication
from .manager import AgentManager

from .perception_agent import PerceptionAgent
from .memory_agent import MemoryAgent
from .reasoning_agent import ReasoningAgent
from .planning_agent import PlanningAgent
from .learning_agent import LearningAgent
from .action_agent import ActionAgent
from .evaluator_agent import EvaluatorAgent

__all__ = [
    "AgentCoordinator",
    "AgentCommunication",
    "AgentManager",
    "PerceptionAgent",
    "MemoryAgent",
    "ReasoningAgent",
    "PlanningAgent",
    "LearningAgent",
    "ActionAgent",
    "EvaluatorAgent",
]

__version__ = "0.1.0"