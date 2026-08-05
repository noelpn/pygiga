# pygiga/safety/validation.py

from dataclasses import dataclass
from typing import Any
import re


@dataclass
class ValidationResult:
    valid: bool
    message: str = ""


class Validator:
    def validate_text(self, text: str) -> ValidationResult:
        if not isinstance(text, str):
            return ValidationResult(False, "Input must be a string.")

        if not text.strip():
            return ValidationResult(False, "Input cannot be empty.")

        return ValidationResult(True, "Valid text.")

    def validate_file_path(self, path: str) -> ValidationResult:
        if ".." in path:
            return ValidationResult(False, "Directory traversal detected.")

        return ValidationResult(True, "Valid path.")

    def validate_url(self, url: str) -> ValidationResult:
        pattern = r"^https?://"

        if not re.match(pattern, url):
            return ValidationResult(False, "Invalid URL.")

        return ValidationResult(True, "Valid URL.")

    def validate_python_code(self, code: str) -> ValidationResult:
        blocked = [
            "os.system",
            "subprocess",
            "eval(",
            "exec(",
            "__import__",
        ]

        for item in blocked:
            if item in code:
                return ValidationResult(
                    False,
                    f"Blocked operation detected: {item}"
                )

        return ValidationResult(True, "Code accepted.")

    def validate_action(self, action: str) -> ValidationResult:
        allowed = {
            "read_file",
            "write_file",
            "internet_access",
            "execute_code",
            "database_read",
            "database_write",
        }

        if action not in allowed:
            return ValidationResult(False, "Unknown action.")

        return ValidationResult(True, "Action allowed.")