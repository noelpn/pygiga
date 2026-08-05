"""
pygiga.communication.prompt
===========================

Prompt Manager

Builds prompts for language models and reasoning engines.

Author: PyGiga
"""

from datetime import datetime
from typing import List, Dict, Optional


class PromptManager:
    """
    Builds prompts for AI models.
    """

    def __init__(self):

        self.system_prompt = (
            "You are PyGiga, an intelligent AI assistant."
        )

        self.prompt_history = []

    # --------------------------------------------------
    # System Prompt
    # --------------------------------------------------

    def set_system_prompt(
        self,
        prompt: str,
    ):

        self.system_prompt = prompt

    def get_system_prompt(self):

        return self.system_prompt

    # --------------------------------------------------
    # Build Prompt
    # --------------------------------------------------

    def build(
        self,
        user_input: str,
        conversation: Optional[List[Dict]] = None,
        memory: Optional[List[Dict]] = None,
    ) -> Dict:

        if conversation is None:
            conversation = []

        if memory is None:
            memory = []

        prompt = {
            "timestamp": datetime.utcnow().isoformat(),
            "system": self.system_prompt,
            "memory": memory,
            "conversation": conversation,
            "user": user_input,
        }

        self.prompt_history.append(prompt)

        return prompt

    # --------------------------------------------------
    # Build Text Prompt
    # --------------------------------------------------

    def build_text(
        self,
        user_input: str,
        conversation: Optional[List[Dict]] = None,
    ) -> str:

        if conversation is None:
            conversation = []

        lines = []

        lines.append(
            f"System: {self.system_prompt}"
        )

        lines.append("")

        for message in conversation:

            role = message.get(
                "role",
                "user",
            ).capitalize()

            content = message.get(
                "content",
                "",
            )

            lines.append(
                f"{role}: {content}"
            )

        lines.append(
            f"User: {user_input}"
        )

        lines.append(
            "Assistant:"
        )

        return "\n".join(lines)

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.prompt_history:
            return None

        return self.prompt_history[-1]

    def history(self):

        return self.prompt_history

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.prompt_history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "prompts_created": len(
                self.prompt_history
            )
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "manager": "PromptManager",
            "system_prompt": self.system_prompt,
            "history": len(
                self.prompt_history
            ),
        }