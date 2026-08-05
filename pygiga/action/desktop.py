"""
pygiga.action.desktop
=====================

Desktop Action Module

Provides desktop operations for PyGiga.

Author: PyGiga
"""

import os
import subprocess
import platform
from pathlib import Path


class DesktopAction:
    """
    Desktop automation utilities.
    """

    def __init__(self):
        self.system = platform.system()

    # ----------------------------
    # Applications
    # ----------------------------

    def open_application(self, application: str):
        """
        Open an application.
        """

        if self.system == "Windows":
            subprocess.Popen(application)

        elif self.system == "Linux":
            subprocess.Popen([application])

        elif self.system == "Darwin":
            subprocess.Popen(["open", "-a", application])

    # ----------------------------
    # Files
    # ----------------------------

    def open_file(self, path: str):
        """
        Open a file with the default application.
        """

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        if self.system == "Windows":
            os.startfile(path)

        elif self.system == "Linux":
            subprocess.Popen(["xdg-open", str(path)])

        elif self.system == "Darwin":
            subprocess.Popen(["open", str(path)])

    def open_folder(self, path: str):
        """
        Open a folder.
        """

        self.open_file(path)

    # ----------------------------
    # URLs
    # ----------------------------

    def open_url(self, url: str):

        if self.system == "Windows":
            os.startfile(url)

        elif self.system == "Linux":
            subprocess.Popen(["xdg-open", url])

        elif self.system == "Darwin":
            subprocess.Popen(["open", url])

    # ----------------------------
    # System
    # ----------------------------

    def current_directory(self):

        return str(Path.cwd())

    def home_directory(self):

        return str(Path.home())

    def list_desktop(self):

        desktop = Path.home() / "Desktop"

        if desktop.exists():
            return [f.name for f in desktop.iterdir()]

        return []

    # ----------------------------
    # Environment
    # ----------------------------

    def environment_variables(self):

        return dict(os.environ)

    # ----------------------------
    # Information
    # ----------------------------

    def info(self):

        return {
            "os": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        }