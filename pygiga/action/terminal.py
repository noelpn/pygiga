"""
pygiga.action.terminal
======================

Terminal Action Module

Execute terminal commands.

Author: PyGiga
"""

import subprocess
import platform
from pathlib import Path
from typing import Dict, List, Optional


class TerminalAction:
    """
    Execute terminal commands.
    """

    def __init__(self):

        self.system = platform.system()

    # --------------------------------------------------
    # Execute
    # --------------------------------------------------

    def run(
        self,
        command: str,
        cwd: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Dict:
        """
        Execute a shell command.
        """

        try:

            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            return {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e),
            }

    # --------------------------------------------------
    # Start Process
    # --------------------------------------------------

    def start(
        self,
        command: str,
        cwd: Optional[str] = None,
    ):
        """
        Start a background process.
        """

        return subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    # --------------------------------------------------
    # Current Directory
    # --------------------------------------------------

    def pwd(self) -> str:

        return str(Path.cwd())

    # --------------------------------------------------
    # Change Directory
    # --------------------------------------------------

    def cd(self, path: str):

        Path(path).resolve()

        return {
            "directory": str(Path(path).resolve())
        }

    # --------------------------------------------------
    # Directory Listing
    # --------------------------------------------------

    def ls(self, path: str = ".") -> List[str]:

        return [
            item.name
            for item in Path(path).iterdir()
        ]

    # --------------------------------------------------
    # Environment
    # --------------------------------------------------

    def whoami(self):

        if self.system == "Windows":
            return self.run("whoami")

        return self.run("whoami")

    def hostname(self):

        if self.system == "Windows":
            return self.run("hostname")

        return self.run("hostname")

    # --------------------------------------------------
    # Python
    # --------------------------------------------------

    def python_version(self):

        return self.run("python --version")

    # --------------------------------------------------
    # Pip
    # --------------------------------------------------

    def pip_list(self):

        return self.run("pip list")

    # --------------------------------------------------
    # Git
    # --------------------------------------------------

    def git_status(self):

        return self.run("git status")

    # --------------------------------------------------
    # System Information
    # --------------------------------------------------

    def info(self):

        return {
            "system": self.system,
            "cwd": self.pwd(),
        }