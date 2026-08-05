"""
pygiga.plugins
==============

Plugin system for PyGiga.

Provides dynamic loading, registration,
and management of PyGiga plugins.
"""

from .plugin import Plugin
from .loader import PluginLoader
from .registry import PluginRegistry

__all__ = [
    "Plugin",
    "PluginLoader",
    "PluginRegistry",
]

__version__ = "0.1.0"