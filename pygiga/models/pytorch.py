"""
pygiga.models.pytorch
=====================

PyTorch backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class PyTorchModel(BaseModel):
    """
    Native PyTorch model backend.
    """

    def __init__(
        self,
        model_name: str = "pytorch-model",
        model: Any = None,
        device: str = "cpu",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.model = model
        self.torch = None

    def load(self) -> None:
        """
        Initialize the PyTorch backend.
        """
        try:
            import torch

            self.torch = torch

            if self.model is not None:
                self.model.to(self.device)
                self.model.eval()

            self.loaded = True

        except ImportError:
            raise ImportError(
                "PyTorch is not installed.\n"
                "Install using:\n"
                "pip install torch"
            )

    def unload(self) -> None:
        """
        Release resources.
        """
        self.model = None
        self.loaded = False

    def set_model(self, model: Any) -> None:
        """
        Assign a PyTorch model.
        """
        self.model = model

        if self.loaded:
            self.model.to(self.device)
            self.model.eval()

    def predict(self, inputs: Any, **kwargs) -> Any:
        """
        Run inference.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError("No PyTorch model has been assigned.")

        with self.torch.no_grad():
            if hasattr(inputs, "to"):
                inputs = inputs.to(self.device)

            return self.model(inputs)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Placeholder for text generation.
        """
        raise NotImplementedError(
            "Generation depends on the assigned PyTorch model."
        )

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Placeholder for embedding generation.
        """
        raise NotImplementedError(
            "Embedding generation depends on the assigned PyTorch model."
        )

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Switch model to training mode.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError("No PyTorch model has been assigned.")

        self.model.train()

    def save(self, path: str) -> None:
        """
        Save the model weights.
        """
        if self.model is None:
            raise RuntimeError("No model available to save.")

        self.torch.save(self.model.state_dict(), path)

    def load_weights(self, path: str) -> None:
        """
        Load model weights.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError("No model has been assigned.")

        state = self.torch.load(
            path,
            map_location=self.device,
        )

        self.model.load_state_dict(state)
        self.model.eval()

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "PyTorch",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "has_model": self.model is not None,
        }