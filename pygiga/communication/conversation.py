"""
pygiga.communication.conversation
=================================

Conversation Manager

Stores and manages conversations.

Author: PyGiga
"""

from datetime import datetime
from typing import List, Dict, Optional


class ConversationManager:
    """
    Manages conversation history.
    """

    def __init__(self):

        self.history: List[Dict] = []

    # --------------------------------------------------
    # Add Messages
    # --------------------------------------------------

    def add_user_message(self, message: str):

        self.history.append({
            "role": "user",
            "content": message,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def add_assistant_message(self, message: str):

        self.history.append({
            "role": "assistant",
            "content": message,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def add_system_message(self, message: str):

        self.history.append({
            "role": "system",
            "content": message,
            "timestamp": datetime.utcnow().isoformat(),
        })

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def latest(self) -> Optional[Dict]:

        if not self.history:
            return None

        return self.history[-1]

    def get_history(self) -> List[Dict]:

        return self.history

    def last(self, count: int = 10) -> List[Dict]:

        return self.history[-count:]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(self, keyword: str) -> List[Dict]:

        keyword = keyword.lower()

        return [
            item
            for item in self.history
            if keyword in item["content"].lower()
        ]

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        users = sum(
            1
            for item in self.history
            if item["role"] == "user"
        )

        assistants = sum(
            1
            for item in self.history
            if item["role"] == "assistant"
        )

        systems = sum(
            1
            for item in self.history
            if item["role"] == "system"
        )

        return {
            "messages": len(self.history),
            "user_messages": users,
            "assistant_messages": assistants,
            "system_messages": systems,
        }

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def remove_last(self):

        if self.history:
            return self.history.pop()

        return None

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.history.clear()

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def export(self):

        return self.history

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "manager": "ConversationManager",
            "messages": len(self.history),
        }