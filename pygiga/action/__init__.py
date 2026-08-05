"""
PyGiga Action Package
=====================

Provides interfaces for executing actions such as:

- Terminal commands
- Browser automation
- File system operations
- Database operations
- API requests
- Email
- Desktop automation
- Mobile automation
- Robotics

Example
-------
from pygiga.action import ActionExecutor
"""

from .executor import ActionExecutor

from .terminal import TerminalAction
from .browser import BrowserAction
from .filesystem import FileSystemAction
from .api import APIAction
from .database import DatabaseAction
from .email import EmailAction
from .desktop import DesktopAction
from .mobile import MobileAction
from .robotics import RoboticsAction

__all__ = [
    "ActionExecutor",
    "TerminalAction",
    "BrowserAction",
    "FileSystemAction",
    "APIAction",
    "DatabaseAction",
    "EmailAction",
    "DesktopAction",
    "MobileAction",
    "RoboticsAction",
]

__version__ = "0.1.0"