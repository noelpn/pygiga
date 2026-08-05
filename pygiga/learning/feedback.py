"""Feedback manager."""

from typing import List

class FeedbackManager:
    """Collects feedback items.""

    def __init__(self):
        self.feedback: List[str] = []

    def add(self, message: str):
        self.feedback.append(message)
        return {'status': 'added', 'message': message}

    def list(self):
        return list(self.feedback)
