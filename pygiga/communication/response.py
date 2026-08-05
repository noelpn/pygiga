"""
pygiga.communication.response
=============================

Response Generator

Responsible for formatting responses.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, Any


class ResponseGenerator:
    """
    Generate responses for the user.
    """

    def __init__(self):

        self.history = []

    # --------------------------------------------------
    # Generate
    # --------------------------------------------------

    def generate(
        self,
        content: Any,
        status: str = "success",
    ) -> Dict:
        """
        Generate a structured response.
        """

        response = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": status,
            "content": content,
        }

        self.history.append(response)

        return response

    # --------------------------------------------------
    # Text
    # --------------------------------------------------

    def text(
        self,
        message: str,
    ) -> Dict:

        return self.generate(
            message,
            "success",
        )

    # --------------------------------------------------
    # Error
    # --------------------------------------------------

    def error(
        self,
        message: str,
    ) -> Dict:

        return self.generate(
            message,
            "error",
        )

    # --------------------------------------------------
    # Warning
    # --------------------------------------------------

    def warning(
        self,
        message: str,
    ) -> Dict:

        return self.generate(
            message,
            "warning",
        )

    # --------------------------------------------------
    # Success
    # --------------------------------------------------

    def success(
        self,
        message: str,
    ) -> Dict:

        return self.generate(
            message,
            "success",
        )

    # --------------------------------------------------
    # JSON
    # --------------------------------------------------

    def json(
        self,
        data: Dict,
    ) -> Dict:

        return self.generate(
            data,
            "success",
        )

    # --------------------------------------------------
    # Latest
    # --------------------------------------------------

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def get_history(self):

        return self.history

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.history.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "responses_generated": len(
                self.history
            )
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "generator": "ResponseGenerator",
            "responses": len(
                self.history
            ),
        }