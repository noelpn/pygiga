"""
pygiga.models.loader
====================

Model loader for PyGiga.

Provides a unified interface for loading models from
different backends.
"""

from typing import Any

from .gemini import GeminiModel
from .huggingface import HuggingFaceModel
from .jax import JAXModel
from .local import LocalModel
from .ollama import OllamaModel
from .openai import OpenAIModel
from .pytorch import PyTorchModel
from .tensorflow import TensorFlowModel


class ModelLoader:
    """
    Unified model loader.
    """

    _BACKENDS = {
        "gemini": GeminiModel,
        "huggingface": HuggingFaceModel,
        "hf": HuggingFaceModel,
        "jax": JAXModel,
        "local": LocalModel,
        "ollama": OllamaModel,
        "openai": OpenAIModel,
        "pytorch": PyTorchModel,
        "torch": PyTorchModel,
        "tensorflow": TensorFlowModel,
        "tf": TensorFlowModel,
    }

    @classmethod
    def available_backends(cls) -> list[str]:
        """
        Return supported backend names.
        """
        return sorted(cls._BACKENDS.keys())

    @classmethod
    def register_backend(
        cls,
        name: str,
        backend: type,
    ) -> None:
        """
        Register a custom backend.
        """
        cls._BACKENDS[name.lower()] = backend

    @classmethod
    def unregister_backend(
        cls,
        name: str,
    ) -> None:
        """
        Remove a backend.
        """
        cls._BACKENDS.pop(name.lower(), None)

    @classmethod
    def load(
        cls,
        backend: str,
        model_name: str,
        auto_load: bool = True,
        **kwargs: Any,
    ):
        """
        Create and optionally load a model.

        Example
        -------
        >>> model = ModelLoader.load(
        ...     "huggingface",
        ...     "gpt2"
        ... )
        """
        backend = backend.lower()

        if backend not in cls._BACKENDS:
            raise ValueError(
                f"Unsupported backend '{backend}'. "
                f"Available: {', '.join(cls.available_backends())}"
            )

        model = cls._BACKENDS[backend](
            model_name=model_name,
            **kwargs,
        )

        if auto_load:
            model.load()

        return model

    @classmethod
    def from_config(cls, config: dict):
        """
        Load a model from a configuration dictionary.

        Example
        -------
        config = {
            "backend": "huggingface",
            "model_name": "gpt2",
            "device": "cuda"
        }
        """
        backend = config.pop("backend")
        model_name = config.pop("model_name")

        return cls.load(
            backend=backend,
            model_name=model_name,
            **config,
        )

    @classmethod
    def is_supported(
        cls,
        backend: str,
    ) -> bool:
        """
        Check whether a backend is supported.
        """
        return backend.lower() in cls._BACKENDS
