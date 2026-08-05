"""General helper utilities."""

from typing import Any, Dict

def safe_get(data, key, default=None):
    if isinstance(data, dict):
        return data.get(key, default)
    return default

def merge_dicts(a: Dict[Any, Any], b: Dict[Any, Any]):
    result = dict(a)
    result.update(b)
    return result
