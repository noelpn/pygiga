"""
pygiga.plugins.loader
=====================

Plugin loader for PyGiga.

Loads plugins dynamically from modules,
files, or directories.
"""

from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Dict, List
import importlib.util
import sys

from .plugin import Plugin


class PluginLoader:
    """
    Dynamic plugin loader.
    """

    def __init__(self):
        self._plugins: Dict[str, Plugin] = {}

    def load_module(
        self,
        module_name: str,
    ) -> Plugin:
        """
        Load a plugin from a Python module.
        """
        module = import_module(module_name)

        plugin = self._find_plugin(module)

        self._plugins[plugin.name] = plugin

        return plugin

    def load_file(
        self,
        file_path: str,
    ) -> Plugin:
        """
        Load a plugin from a Python file.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        spec = importlib.util.spec_from_file_location(
            path.stem,
            path,
        )

        module = importlib.util.module_from_spec(spec)

        sys.modules[path.stem] = module

        spec.loader.exec_module(module)

        plugin = self._find_plugin(module)

        self._plugins[plugin.name] = plugin

        return plugin

    def load_directory(
        self,
        directory: str,
    ) -> List[Plugin]:
        """
        Load every plugin in a directory.
        """
        directory = Path(directory)

        plugins = []

        for file in directory.glob("*.py"):
            if file.name.startswith("_"):
                continue

            try:
                plugins.append(
                    self.load_file(str(file))
                )
            except Exception:
                continue

        return plugins

    def unload(
        self,
        name: str,
    ) -> None:
        """
        Unload a plugin.
        """
        self._plugins.pop(name, None)

    def get(
        self,
        name: str,
    ) -> Plugin:
        """
        Return a loaded plugin.
        """
        if name not in self._plugins:
            raise KeyError(
                f"Plugin '{name}' not loaded."
            )

        return self._plugins[name]

    def plugins(self) -> List[str]:
        """
        Return loaded plugin names.
        """
        return sorted(self._plugins.keys())

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a plugin is loaded.
        """
        return name in self._plugins

    def clear(self) -> None:
        """
        Unload every plugin.
        """
        self._plugins.clear()

    def _find_plugin(
        self,
        module: ModuleType,
    ) -> Plugin:
        """
        Locate the Plugin instance inside a module.
        """
        for obj in module.__dict__.values():
            if isinstance(obj, Plugin):
                return obj

        raise RuntimeError(
            "No Plugin instance found."
        )

    def info(self):
        """
        Return loader information.
        """
        return {
            "loaded_plugins": len(self._plugins),
            "plugins": self.plugins(),
        }

    def __len__(self):
        return len(self._plugins)

    def __contains__(self, name: str):
        return name in self._plugins

    def __repr__(self):
        return (
            f"PluginLoader("
            f"plugins={len(self._plugins)})"
        )