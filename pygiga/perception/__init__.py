"""
pygiga.perception
=================

Perception module for PyGiga.

Provides interfaces for processing multiple input modalities,
including text, images, audio, speech, documents, sensors,
and multimodal data.
"""

from .audio import AudioPerception
from .document import DocumentPerception
from .multimodal import MultiModalPerception
from .sensor import SensorPerception
from .speech import SpeechPerception
from .text import TextPerception
from .vision import VisionPerception

__all__ = [
    "AudioPerception",
    "DocumentPerception",
    "MultiModalPerception",
    "SensorPerception",
    "SpeechPerception",
    "TextPerception",
    "VisionPerception",
]

__version__ = "0.1.0"