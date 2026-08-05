"""
pygiga.models.ollama
====================

Ollama backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class OllamaModel(BaseModel):
    """
    Ollama model backend.
    """

    def __init__(
        self,
        model_name: str = "llama3",
        host: str = "http://localhost:11434",
        device: str = "local",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.host = host
        self.client = None

    def load(self) -> None:
        """
        Initialize the Ollama client.
        """
        try:
            from ollama import Client

            self.client = Client(host=self.host)
            self.loaded = True

        except ImportError:
            raise ImportError(
                "Ollama Python package is not installed.\n"
                "Install using:\n"
                "pip install ollama"
            )

    def unload(self) -> None:
        """
        Release resources.
        """
        self.client = None
        self.loaded = False

    def predict(self, inputs: Any, **kwargs) -> Any:
        """
        Alias for generate().
        """
        return self.generate(str(inputs), **kwargs)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text using Ollama.
        """
        if not self.loaded:
            self.load()

        response = self.client.generate(
            model=self.model_name,
            prompt=prompt,
            **kwargs,
        )

        return response["response"]

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Generate embeddings.
        """
        if not self.loaded:
            self.load()

        response = self.client.embeddings(
            model=self.model_name,
            prompt=text,
            **kwargs,
        )

        return response["embedding"]

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Ollama does not support training.
        """
        raise NotImplementedError(
            "Training is not supported through the Ollama API."
        )

    def save(self, path: str) -> None:
        """
        Saving Ollama models is unsupported.
        """
        raise NotImplementedError(
            "Ollama manages models internally and cannot export them through the API."
        )

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "Ollama",
            "model": self.model_name,
            "host": self.host,
            "device": self.device,
            "loaded": self.loaded,
            "local": True,
        }