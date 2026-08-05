"""Configuration helpers."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

@dataclass
class Config:
    app_name: str = 'pygiga'
    version: str = '0.1.0'
    debug: bool = False
    settings: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Optional[str] = None):
        config = cls()
        if path:
            try:
                data = json.loads(Path(path).read_text(encoding='utf-8'))
                config.settings.update(data)
            except Exception:
                pass
        config.settings.update({k: v for k, v in dict(**__import__('os').environ).items()})
        return config
