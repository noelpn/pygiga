"""
pygiga.perception.speech
========================

Speech perception module for PyGiga.

Provides speech-to-text (STT), text-to-speech (TTS),
language detection, and speech processing utilities.
"""

from pathlib import Path
from typing import Any, Dict


class SpeechPerception:
    """
    Speech perception interface.
    """

    def __init__(self):
        pass

    def transcribe(
        self,
        audio_path: str,
        model: Any = None,
        **kwargs,
    ) -> str:
        """
        Convert speech to text.

        If a model is supplied, it must implement
        transcribe().
        """
        if model is None:
            raise ValueError(
                "A speech recognition model is required."
            )

        if not hasattr(model, "transcribe"):
            raise ValueError(
                "Model must implement transcribe()."
            )

        return model.transcribe(audio_path, **kwargs)

    def synthesize(
        self,
        text: str,
        model: Any = None,
        **kwargs,
    ):
        """
        Convert text to speech.

        If a model is supplied, it must implement
        generate().
        """
        if model is None:
            raise ValueError(
                "A text-to-speech model is required."
            )

        if not hasattr(model, "generate"):
            raise ValueError(
                "Model must implement generate()."
            )

        return model.generate(text, **kwargs)

    def language(
        self,
        text: str,
    ) -> str:
        """
        Detect language.
        """
        try:
            from langdetect import detect

            return detect(text)

        except ImportError:
            raise ImportError(
                "langdetect is not installed.\n"
                "Install using:\n"
                "pip install langdetect"
            )

    def duration(
        self,
        audio_path: str,
    ) -> float:
        """
        Return audio duration.
        """
        try:
            import librosa

            audio, sr = librosa.load(
                audio_path,
                sr=None,
            )

            return len(audio) / sr

        except ImportError:
            raise ImportError(
                "librosa is required.\n"
                "Install using:\n"
                "pip install librosa"
            )

    def exists(
        self,
        audio_path: str,
    ) -> bool:
        """
        Check whether an audio file exists.
        """
        return Path(audio_path).exists()

    def info(
        self,
        audio_path: str,
    ) -> Dict[str, Any]:
        """
        Return information about an audio file.
        """
        path = Path(audio_path)

        return {
            "path": str(path),
            "name": path.name,
            "extension": path.suffix,
            "size_bytes": path.stat().st_size
            if path.exists()
            else 0,
            "exists": path.exists(),
        }

    def __repr__(self):
        return "SpeechPerception()"