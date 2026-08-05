"""
pygiga.plugins.plugin
=====================

Base plugin class for PyGiga.

Every plugin should inherit from this class.
"""

from abc import ABC
from typing import Any, Dict


class Plugin(ABC):
    """
    Base plugin interface.
    """

    def __init__(
        self,
        name: str,
        version: str = "1.0.0",
        author: str = "Unknown",
        description: str = "",
    ):
        self.name = name
        self.version = version
        self.author = author
        self.description = description
        self.enabled = False

    def enable(self) -> None:
        """
        Enable the plugin.
        """
        self.enabled = True

    def disable(self) -> None:
        """
        Disable the plugin.
        """
        self.enabled = False

    def toggle(self) -> None:
        """
        Toggle the plugin state.
        """
        self.enabled = not self.enabled

    def initialize(self, *args, **kwargs) -> None:
        """
        Initialize the plugin.

        Override this method in subclasses.
        """
        pass

    def shutdown(self) -> None:
        """
        Shutdown the plugin.

        Override this method in subclasses.
        """
        pass

    def execute(
        self,
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute the plugin.

        Override this method in subclasses.
        """
        raise NotImplementedError(
            "Plugins must implement execute()."
        )

    def configure(
        self,
        **settings,
    ) -> None:
        """
        Update plugin configuration.
        """
        for key, value in settings.items():
            setattr(self, key, value)

    def info(self) -> Dict[str, Any]:
        """
        Return plugin information.
        """
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
            "enabled": self.enabled,
        }

    def __repr__(self):
        return (
            f"Plugin("
            f"name='{self.name}', "
            f"version='{self.version}', "
            f"enabled={self.enabled})"
        )