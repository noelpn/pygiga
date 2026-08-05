"""
pygiga.plugins.registry
=======================

Plugin registry for PyGiga.

Maintains a registry of installed plugins and provides
utilities for registering, unregistering, and retrieving
plugins.
"""

from typing import Dict, List

from .plugin import Plugin


class PluginRegistry:
    """
    Registry for PyGiga plugins.
    """

    def __init__(self):
        self._plugins: Dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
        overwrite: bool = False,
    ) -> None:
        """
        Register a plugin.
        """
        if not isinstance(plugin, Plugin):
            raise TypeError(
                "plugin must be an instance of Plugin."
            )

        if (
            plugin.name in self._plugins
            and not overwrite
        ):
            raise ValueError(
                f"Plugin '{plugin.name}' is already registered."
            )

        self._plugins[plugin.name] = plugin

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove a plugin from the registry.
        """
        self._plugins.pop(name, None)

    def get(
        self,
        name: str,
    ) -> Plugin:
        """
        Return a registered plugin.
        """
        if name not in self._plugins:
            raise KeyError(
                f"Plugin '{name}' is not registered."
            )

        return self._plugins[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a plugin exists.
        """
        return name in self._plugins

    def enable(
        self,
        name: str,
    ) -> None:
        """
        Enable a plugin.
        """
        self.get(name).enable()

    def disable(
        self,
        name: str,
    ) -> None:
        """
        Disable a plugin.
        """
        self.get(name).disable()

    def names(self) -> List[str]:
        """
        Return registered plugin names.
        """
        return sorted(self._plugins.keys())

    def plugins(self) -> List[Plugin]:
        """
        Return all registered plugins.
        """
        return list(self._plugins.values())

    def clear(self) -> None:
        """
        Remove all registered plugins.
        """
        self._plugins.clear()

    def info(self):
        """
        Return registry information.
        """
        return {
            "registered_plugins": len(self._plugins),
            "plugins": self.names(),
        }

    def __len__(self):
        return len(self._plugins)

    def __contains__(self, name: str):
        return name in self._plugins

    def __iter__(self):
        return iter(self._plugins.values())

    def __repr__(self):
        return (
            f"PluginRegistry("
            f"plugins={len(self._plugins)})"
        )