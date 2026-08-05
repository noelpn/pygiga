"""
pygiga.action.browser
=====================

Browser Action Module

Provides simple browser operations.

Author: PyGiga
"""

import webbrowser
from urllib.parse import quote_plus


class BrowserAction:
    """
    Browser utility class.
    """

    def __init__(self):
        pass

    def open(self, url: str) -> bool:
        """
        Open a URL in the default web browser.
        """
        return webbrowser.open(url)

    def open_new_tab(self, url: str) -> bool:
        """
        Open a URL in a new browser tab.
        """
        return webbrowser.open_new_tab(url)

    def open_new_window(self, url: str) -> bool:
        """
        Open a URL in a new browser window.
        """
        return webbrowser.open_new(url)

    def search_google(self, query: str) -> bool:
        """
        Search Google.
        """
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        return self.open_new_tab(url)

    def search_bing(self, query: str) -> bool:
        """
        Search Bing.
        """
        url = f"https://www.bing.com/search?q={quote_plus(query)}"
        return self.open_new_tab(url)

    def search_duckduckgo(self, query: str) -> bool:
        """
        Search DuckDuckGo.
        """
        url = f"https://duckduckgo.com/?q={quote_plus(query)}"
        return self.open_new_tab(url)