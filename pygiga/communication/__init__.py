"""
pygiga.communication
====================

Human Communication Package

Provides language understanding, dialogue management,
conversation history, prompts, and response generation.

Author: PyGiga
"""

from .language import LanguageProcessor
from .dialogue import DialogueManager
from .conversation import ConversationManager
from .prompt import PromptManager
from .response import ResponseGenerator

__all__ = [
    "LanguageProcessor",
    "DialogueManager",
    "ConversationManager",
    "PromptManager",
    "ResponseGenerator",
]

__version__ = "0.1.0"