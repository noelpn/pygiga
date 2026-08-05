"""Configuration helpers."""

import json
from pathlib import Path

def load_config(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except Exception:
        return {}
