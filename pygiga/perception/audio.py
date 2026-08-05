"""
pygiga.perception.audio
=======================

Audio perception module for PyGiga.

Provides utilities for loading, preprocessing, analyzing,
and transcribing audio.
"""

from pathlib import Path
from typing import Any, Dict, Optional


class AudioPerception:
    """
    Audio perception interface.
    """

    def __init__(
        self,
        sample_rate: int = 16000,
        channels: int = 1,
    ):
        self.sample_rate = sample_rate
        self.channels = channels

    def load(self, path: str):
        """
        Load an audio file.
        """
        try:
            import librosa

            audio, sr = librosa.load(
                path,
                sr=self.sample_rate,
                mono=self.channels == 1,
            )

            return audio, sr

        except ImportError:
            raise ImportError(
                "librosa is not installed.\n"
                "Install using:\n"
                "pip install librosa"
            )

    def save(
        self,
        path: str,
        audio: Any,
        sample_rate: Optional[int] = None,
    ) -> None:
        """
        Save an audio file.
        """
        try:
            import soundfile as sf

            sf.write(
                path,
                audio,
                sample_rate or self.sample_rate,
            )

        except ImportError:
            raise ImportError(
                "soundfile is not installed.\n"
                "Install using:\n"
                "pip install soundfile"
            )

    def duration(self, path: str) -> float:
        """
        Return audio duration in seconds.
        """
        audio, sr = self.load(path)
        return len(audio) / sr

    def features(self, path: str):
        """
        Extract MFCC features.
        """
        try:
            import librosa

            audio, sr = self.load(path)

            return librosa.feature.mfcc(
                y=audio,
                sr=sr,
                n_mfcc=13,
            )

        except ImportError:
            raise ImportError(
                "librosa is required."
            )

    def transcribe(
        self,
        path: str,
        model: Any,
        **kwargs,
    ) -> str:
        """
        Transcribe speech using a supplied model.
        """
        if not hasattr(model, "transcribe"):
            raise ValueError(
                "Model must implement transcribe()."
            )

        return model.transcribe(path, **kwargs)

    def classify(
        self,
        path: str,
        model: Any,
        **kwargs,
    ):
        """
        Classify audio using a supplied model.
        """
        if not hasattr(model, "predict"):
            raise ValueError(
                "Model must implement predict()."
            )

        audio, _ = self.load(path)

        return model.predict(audio, **kwargs)

    def info(self, path: str) -> Dict[str, Any]:
        """
        Return audio information.
        """
        audio, sr = self.load(path)

        return {
            "path": str(Path(path)),
            "sample_rate": sr,
            "samples": len(audio),
            "duration": len(audio) / sr,
            "channels": self.channels,
        }

    def __repr__(self):
        return (
            f"AudioPerception("
            f"sample_rate={self.sample_rate}, "
            f"channels={self.channels})"
        )