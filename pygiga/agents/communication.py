"""
pygiga.agents.communication
===========================

Internal Agent Communication System

Provides message passing between PyGiga agents.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Any


class AgentCommunication:
    """
    Communication bus for agents.
    """

    def __init__(self):

        self.messages: List[Dict[str, Any]] = []

    # --------------------------------------------------
    # Send
    # --------------------------------------------------

    def send(
        self,
        sender: str,
        receiver: str,
        message: Any,
    ) -> Dict[str, Any]:
        """
        Send a message.
        """

        packet = {
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.messages.append(packet)

        return packet

    # --------------------------------------------------
    # Receive
    # --------------------------------------------------

    def receive(
        self,
        receiver: str,
    ) -> List[Dict[str, Any]]:
        """
        Get all messages for an agent.
        """

        inbox = [
            msg
            for msg in self.messages
            if msg["receiver"] == receiver
        ]

        return inbox

    # --------------------------------------------------
    # Broadcast
    # --------------------------------------------------

    def broadcast(
        self,
        sender: str,
        message: Any,
    ) -> Dict[str, Any]:
        """
        Broadcast a message.
        """

        packet = {
            "sender": sender,
            "receiver": "ALL",
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.messages.append(packet)

        return packet

    # --------------------------------------------------
    # Clear Inbox
    # --------------------------------------------------

    def clear(
        self,
        receiver: str,
    ):
        """
        Remove messages already processed.
        """

        self.messages = [
            msg
            for msg in self.messages
            if msg["receiver"] != receiver
        ]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def history(self):

        return self.messages

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def stats(self):

        return {
            "messages": len(self.messages)
        }