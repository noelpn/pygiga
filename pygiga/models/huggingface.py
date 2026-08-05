"""
pygiga.models.huggingface
=========================

Hugging Face backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class HuggingFaceModel(BaseModel):
    """
    Hugging Face Transformers backend.
    """

    def __init__(
        self,
        model_name: str = "gpt2",
        device: str = "cpu",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.tokenizer = None
        self.model = None
        self.pipeline = None

    def load(self) -> None:
        """
        Load a Hugging Face model.
        """
        try:
            from transformers import (
                AutoTokenizer,
                AutoModel,
                AutoModelForCausalLM,
                pipeline,
            )
            import torch

            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

            try:
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name
                )
            except Exception:
                self.model = AutoModel.from_pretrained(
                    self.model_name
                )

            device = 0 if (
                self.device == "cuda" and torch.cuda.is_available()
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

        max_new_tokens = kwargs.pop("max_new_tokens", 100)

        result = self.pipeline(
            prompt,
            max_new_tokens=max_new_tokens,
            **kwargs,
        )

        return result[0]["generated_text"]

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Generate sentence embedding.
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
        Placeholder for fine-tuning.
        """
        raise NotImplementedError(
            "Use PyGiga Trainer for Hugging Face fine-tuning."
        )

    def save(self, path: str) -> None:
        """
        Save model locally.
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
            "backend": "HuggingFace",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "local": True,
        }