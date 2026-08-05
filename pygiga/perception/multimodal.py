"""
pygiga.perception.multimodal
============================

Multimodal perception module for PyGiga.

Combines multiple perception modules (text, vision, audio,
speech, documents, sensors) into a unified interface.
"""

from typing import Any, Dict

from .audio import AudioPerception
from .document import DocumentPerception
from .sensor import SensorPerception
from .speech import SpeechPerception
from .text import TextPerception
from .vision import VisionPerception


class MultiModalPerception:
    """
    Unified multimodal perception interface.
    """

    def __init__(self):
        self.text = TextPerception()
        self.vision = VisionPerception()
        self.audio = AudioPerception()
        self.speech = SpeechPerception()
        self.document = DocumentPerception()
        self.sensor = SensorPerception()

    def process(
        self,
        modality: str,
        source: Any,
        **kwargs,
    ):
        """
        Process input based on modality.
        """
        modality = modality.lower()

        if modality == "text":
            return self.text.process(source, **kwargs)

        elif modality == "vision":
            return self.vision.process(source, **kwargs)

        elif modality == "image":
            return self.vision.process(source, **kwargs)

        elif modality == "audio":
            return self.audio.load(source)

        elif modality == "speech":
            return self.speech.transcribe(
                source,
                **kwargs,
            )

        elif modality == "document":
            return self.document.load(source)

        elif modality == "sensor":
            return self.sensor.read(source)

        raise ValueError(
            f"Unsupported modality '{modality}'."
        )

    def process_all(
        self,
        **modalities,
    ) -> Dict[str, Any]:
        """
        Process multiple modalities.

        Example
        -------
        perception.process_all(
            text="Hello",
            image="cat.png",
            document="paper.pdf"
        )
        """
        results = {}

        for modality, value in modalities.items():
            try:
                results[modality] = self.process(
                    modality,
                    value,
                )
            except Exception as e:
                results[modality] = {
                    "error": str(e)
                }

        return results

    def available_modalities(self):
        """
        Return supported modalities.
        """
        return [
            "text",
            "vision",
            "image",
            "audio",
            "speech",
            "document",
            "sensor",
        ]

    def info(self) -> Dict[str, Any]:
        """
        Return module information.
        """
        return {
            "module": "MultiModalPerception",
            "modalities": self.available_modalities(),
            "count": len(self.available_modalities()),
        }

    def __repr__(self):
        return (
            f"MultiModalPerception("
            f"modalities={len(self.available_modalities())})"
        )