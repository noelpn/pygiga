"""Cache utilities."""

class Cache:
    """Simple in-memory cache."""

    def __init__(self):
        self.storage = {}

    def set(self, key, value):
        self.storage[key] = value

    def get(self, key, default=None):
        return self.storage.get(key, default)

    def clear(self):
        self.storage.clear()
