"""
pygiga.models.tensorflow
========================

TensorFlow backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class TensorFlowModel(BaseModel):
    """
    Native TensorFlow/Keras model backend.
    """

    def __init__(
        self,
        model_name: str = "tensorflow-model",
        model: Any = None,
        device: str = "cpu",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.model = model
        self.tf = None

    def load(self) -> None:
        """
        Initialize the TensorFlow backend.
        """
        try:
            import tensorflow as tf

            self.tf = tf

            self.loaded = True

        except ImportError:
            raise ImportError(
                "TensorFlow is not installed.\n"
                "Install using:\n"
                "pip install tensorflow"
            )

    def unload(self) -> None:
        """
        Release resources.
        """
        self.model = None
        self.loaded = False

    def set_model(self, model: Any) -> None:
        """
        Assign a TensorFlow/Keras model.
        """
        self.model = model

    def predict(self, inputs: Any, **kwargs) -> Any:
        """
        Run inference.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError(
                "No TensorFlow model has been assigned."
            )

        return self.model.predict(inputs, **kwargs)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Placeholder for text generation.
        """
        raise NotImplementedError(
            "Generation depends on the assigned TensorFlow model."
        )

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Placeholder for embedding generation.
        """
        raise NotImplementedError(
            "Embedding generation depends on the assigned TensorFlow model."
        )

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Train the assigned model.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError(
                "No TensorFlow model has been assigned."
            )

        self.model.fit(dataset, **kwargs)

    def save(self, path: str) -> None:
        """
        Save the TensorFlow model.
        """
        if self.model is None:
            raise RuntimeError(
                "No model available to save."
            )

        self.model.save(path)

    def load_weights(self, path: str) -> None:
        """
        Load model weights.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError(
                "No model has been assigned."
            )

        self.model.load_weights(path)

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "TensorFlow",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "has_model": self.model is not None,
        }