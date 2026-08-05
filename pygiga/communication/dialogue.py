"""
pygiga.communication.dialogue
=============================

Dialogue Manager

Controls the flow of conversations.

Author: PyGiga
"""

from datetime import datetime


class DialogueManager:
    """
    Manages dialogue state.
    """

    def __init__(self):

        self.state = "idle"
        self.history = []

    # --------------------------------------------------
    # Update State
    # --------------------------------------------------

    def update(self, user_input: str):

        state = self.detect_state(user_input)

        self.state = state

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": user_input,
            "state": state,
        }

        self.history.append(event)

        return event

    # --------------------------------------------------
    # Detect Dialogue State
    # --------------------------------------------------

    def detect_state(self, text: str):

        if not text:
            return "idle"

        text = text.lower().strip()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
        ]

        farewells = [
            "bye",
            "goodbye",
            "exit",
            "quit",
        ]

        if any(text.startswith(word) for word in greetings):
            return "greeting"

        if any(text.startswith(word) for word in farewells):
            return "ending"

        if text.endswith("?"):
            return "question"

        return "conversation"

    # --------------------------------------------------
    # Current State
    # --------------------------------------------------

    def current_state(self):

        return self.state

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def get_history(self):

        return self.history

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.state = "idle"
        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        counts = {}

        for item in self.history:

            state = item["state"]

            counts[state] = counts.get(state, 0) + 1

        return counts

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "manager": "DialogueManager",
            "state": self.state,
            "events": len(self.history),
        }