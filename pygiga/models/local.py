"""
pygiga.models.local
===================

Local model backend for PyGiga.

Loads models stored on the local filesystem.
"""

from pathlib import Path
from typing import Any, Dict, List

from .base import BaseModel


class LocalModel(BaseModel):
    """
    Local model backend.
    """

    def __init__(
        self,
        model_name: str,
        model_path: str | None = None,
        device: str = "cpu",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.model_path = Path(model_path) if model_path else None
        self.model = None
        self.tokenizer = None

    def load(self) -> None:
        """
        Load a local model.
        """
        if self.model_path is None:
            raise ValueError("model_path is required.")

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model path not found: {self.model_path}"
            )

        try:
            from transformers import (
                AutoModelForCausalLM,
                AutoTokenizer,
                pipeline,
            )
            import torch

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_path
            )

            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path
            )

            device = 0 if (
                self.device == "cuda"
                and torch.cuda.is_available()
            ) else -1

            self.pipeline = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                device=device,
            )

            self.loaded = True

        except ImportError:
            raise ImportError(
                "transformers is not installed.\n"
                "Install using:\n"
                "pip install transformers torch"
            )

    def unload(self) -> None:
        """
        Release resources.
        """
        self.model = None
        self.tokenizer = None
        self.pipeline = None
        self.loaded = False

    def predict(self, inputs: Any, **kwargs) -> Any:
        """
        Alias for generate().
        """
        return self.generate(str(inputs), **kwargs)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text.
        """
        if not self.loaded:
            self.load()

        result = self.pipeline(
            prompt,
            max_new_tokens=kwargs.pop("max_new_tokens", 100),
            **kwargs,
        )

        return result[0]["generated_text"]

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Generate embeddings.
        """
        if not self.loaded:
            self.load()

        import torch

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        embedding = outputs.last_hidden_state.mean(dim=1)

        return embedding.squeeze().tolist()

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Local backend does not implement training.
        """
        raise NotImplementedError(
            "Use the PyGiga training module."
        )

    def save(self, path: str) -> None:
        """
        Save the model.
        """
        if not self.loaded:
            self.load()

        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def info(self) -> Dict[str, Any]:
        """
        Return model information.
        """
        return {
            "backend": "Local",
            "model": self.model_name,
            "path": str(self.model_path),
            "device": self.device,
            "loaded": self.loaded,
        }
