"""Serialization helpers."""

import json

def to_json(value):
    return json.dumps(value, default=str)

def from_json(text):
    return json.loads(text)
