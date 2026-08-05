"""
pygiga.models.gemini
====================

Google Gemini backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class GeminiModel(BaseModel):
    """
    Google Gemini model backend.
    """

    def __init__(
        self,
        model_name: str = "gemini-2.5-pro",
        api_key: str | None = None,
        device: str = "cloud",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.api_key = api_key
        self.client = None

    def load(self) -> None:
        """
        Initialize the Gemini client.
        """
        try:
            from google import genai

            self.client = genai.Client(api_key=self.api_key)
            self.loaded = True

        except ImportError:
            raise ImportError(
                "Google GenAI SDK is not installed.\n"
                "Install it using:\n"
                "pip install google-genai"
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
        Generate text using Gemini.
        """
        if not self.loaded:
            self.load()

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            **kwargs,
        )

        return response.text

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Generate embeddings.
        """
        if not self.loaded:
            self.load()

        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
            **kwargs,
        )

        return list(response.embeddings[0].values)

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Gemini does not support local training.
        """
        raise NotImplementedError(
            "Gemini models cannot be trained through the public API."
        )

    def save(self, path: str) -> None:
        """
        Saving cloud models is unsupported.
        """
        raise NotImplementedError(
            "Cloud-hosted Gemini models cannot be saved locally."
        )

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "Gemini",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "cloud": True,
        }