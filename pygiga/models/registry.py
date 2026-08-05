"""
pygiga.models.registry
======================

Model registry for PyGiga.

Keeps track of all available model backends and allows
custom backends to be registered.
"""

from typing import Dict, List, Type

from .base import BaseModel
from .gemini import GeminiModel
from .huggingface import HuggingFaceModel
from .jax import JAXModel
from .local import LocalModel
from .ollama import OllamaModel
from .openai import OpenAIModel
from .pytorch import PyTorchModel
from .tensorflow import TensorFlowModel


class ModelRegistry:
    """
    Registry of all available model backends.
    """

    _registry: Dict[str, Type[BaseModel]] = {
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
    def register(
        cls,
        name: str,
        backend: Type[BaseModel],
        overwrite: bool = False,
    ) -> None:
        """
        Register a backend.

        Example
        -------
        ModelRegistry.register(
            "mybackend",
            MyBackend
        )
        """
        name = name.lower()

        if name in cls._registry and not overwrite:
            raise ValueError(
                f"Backend '{name}' is already registered."
            )

        cls._registry[name] = backend

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Remove a backend.
        """
        cls._registry.pop(name.lower(), None)

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseModel]:
        """
        Return a backend class.
        """
        name = name.lower()

        if name not in cls._registry:
            raise KeyError(
                f"Backend '{name}' is not registered."
            )

        return cls._registry[name]

    @classmethod
    def create(
        cls,
        backend: str,
        model_name: str,
        **kwargs,
    ) -> BaseModel:
        """
        Create a backend instance.
        """
        backend_cls = cls.get(backend)

        return backend_cls(
            model_name=model_name,
            **kwargs,
        )

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Check whether a backend exists.
        """
        return name.lower() in cls._registry

    @classmethod
    def names(cls) -> List[str]:
        """
        Return registered backend names.
        """
        return sorted(cls._registry.keys())

    @classmethod
    def backends(cls) -> Dict[str, Type[BaseModel]]:
        """
        Return a copy of the registry.
        """
        return cls._registry.copy()

    @classmethod
    def clear(cls) -> None:
        """
        Remove all registered backends.
        """
        cls._registry.clear()

    @classmethod
    def reset(cls) -> None:
        """
        Restore the default registry.
        """
        cls._registry = {
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

    def __contains__(self, name: str) -> bool:
        return self.exists(name)

    def __len__(self) -> int:
        return len(self._registry)

    def __repr__(self) -> str:
        return (
            f"ModelRegistry("
            f"backends={len(self._registry)})"
        )