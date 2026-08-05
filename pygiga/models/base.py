"""
pygiga.models.base
==================

Base model interface for all PyGiga model backends.
Every backend (OpenAI, Gemini, Ollama, Hugging Face,
PyTorch, TensorFlow, JAX, Local) should inherit from
BaseModel.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseModel(ABC):
    """
    Abstract base class for all PyGiga models.
    """

    def __init__(
        self,
        model_name: str,
        device: str = "cpu",
        **kwargs
    ):
        self.model_name = model_name
        self.device = device
        self.config = kwargs
        self.loaded = False

    @abstractmethod
    def load(self) -> None:
        """
        Load the model into memory.
        """
        raise NotImplementedError

    @abstractmethod
    def unload(self) -> None:
        """
        Release model resources.
        """
        raise NotImplementedError

    @abstractmethod
    def predict(
        self,
        inputs: Any,
        **kwargs
    ) -> Any:
        """
        Run inference.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        prompt: str,
        **kwargs
    ) -> str:
        """
        Generate text from a prompt.
        """
        raise NotImplementedError

    @abstractmethod
    def embed(
        self,
        text: str,
        **kwargs
    ) -> List[float]:
        """
        Generate text embeddings.
        """
        raise NotImplementedError

    @abstractmethod
    def train(
        self,
        dataset: Any,
        **kwargs
    ) -> None:
        """
        Train or fine-tune the model.
        """
        raise NotImplementedError

    @abstractmethod
    def save(
        self,
        path: str
    ) -> None:
        """
        Save the model.
        """
        raise NotImplementedError

    @abstractmethod
    def info(self) -> Dict[str, Any]:
        """
        Return model information.
        """
        raise NotImplementedError

    def is_loaded(self) -> bool:
        """
        Check whether the model is loaded.
        """
        return self.loaded

    def __repr__(self) -> str:
        status = "Loaded" if self.loaded else "Not Loaded"
        return (
            f"{self.__class__.__name__}"
            f"(model='{self.model_name}', "
            f"device='{self.device}', "
            f"status='{status}')"
        )