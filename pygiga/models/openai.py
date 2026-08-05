"""
pygiga.models.openai
====================

OpenAI backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class OpenAIModel(BaseModel):
    """
    OpenAI model backend.
    """

    def __init__(
        self,
        model_name: str = "gpt-4.1",
        api_key: str | None = None,
        device: str = "cloud",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.api_key = api_key
        self.client = None

    def load(self) -> None:
        """
        Initialize the OpenAI client.
        """
        try:
            from openai import OpenAI

            self.client = OpenAI(api_key=self.api_key)
            self.loaded = True

        except ImportError:
            raise ImportError(
                "OpenAI SDK is not installed.\n"
                "Install using:\n"
                "pip install openai"
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
        Generate text using an OpenAI model.
        """
        if not self.loaded:
            self.load()

        response = self.client.responses.create(
            model=self.model_name,
            input=prompt,
            **kwargs,
        )

        return response.output_text

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Generate embeddings.
        """
        if not self.loaded:
            self.load()

        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
            **kwargs,
        )

        return response.data[0].embedding

    def train(self, dataset: Any, **kwargs) -> None:
        """
        OpenAI public models cannot be trained directly.
        """
        raise NotImplementedError(
            "Training OpenAI foundation models is not supported through the public API."
        )

    def save(self, path: str) -> None:
        """
        Saving cloud-hosted models is unsupported.
        """
        raise NotImplementedError(
            "Cloud-hosted OpenAI models cannot be saved locally."
        )

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "OpenAI",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "cloud": True,
        }