"""
pygiga.models.jax
=================

JAX backend for PyGiga.
"""

from typing import Any, Dict, List

from .base import BaseModel


class JAXModel(BaseModel):
    """
    JAX model backend.
    """

    def __init__(
        self,
        model_name: str = "jax-model",
        device: str = "cpu",
        **kwargs,
    ):
        super().__init__(model_name=model_name, device=device, **kwargs)

        self.model = None
        self.params = None
        self.jax = None
        self.jnp = None

    def load(self) -> None:
        """
        Initialize the JAX backend.
        """
        try:
            import jax
            import jax.numpy as jnp

            self.jax = jax
            self.jnp = jnp

            self.loaded = True

        except ImportError:
            raise ImportError(
                "JAX is not installed.\n"
                "Install using:\n"
                "pip install jax jaxlib"
            )

    def unload(self) -> None:
        """
        Release resources.
        """
        self.model = None
        self.params = None
        self.loaded = False

    def predict(self, inputs: Any, **kwargs) -> Any:
        """
        Run inference.
        """
        if not self.loaded:
            self.load()

        if self.model is None:
            raise RuntimeError("No JAX model has been assigned.")

        return self.model.apply(self.params, inputs)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Placeholder for text generation.
        """
        raise NotImplementedError(
            "Text generation depends on the loaded JAX model."
        )

    def embed(self, text: str, **kwargs) -> List[float]:
        """
        Placeholder for embedding generation.
        """
        raise NotImplementedError(
            "Embedding generation depends on the loaded JAX model."
        )

    def train(self, dataset: Any, **kwargs) -> None:
        """
        Placeholder for training.
        """
        raise NotImplementedError(
            "Use the PyGiga training module for JAX model training."
        )

    def save(self, path: str) -> None:
        """
        Save model parameters.
        """
        if self.params is None:
            raise RuntimeError("No parameters available to save.")

        try:
            import pickle

            with open(path, "wb") as f:
                pickle.dump(self.params, f)

        except Exception as e:
            raise RuntimeError(f"Failed to save parameters: {e}")

    def load_parameters(self, path: str) -> None:
        """
        Load saved model parameters.
        """
        try:
            import pickle

            with open(path, "rb") as f:
                self.params = pickle.load(f)

        except Exception as e:
            raise RuntimeError(f"Failed to load parameters: {e}")

    def set_model(self, model: Any, params: Any = None) -> None:
        """
        Assign a JAX model and its parameters.
        """
        self.model = model
        self.params = params

    def info(self) -> Dict[str, Any]:
        """
        Return backend information.
        """
        return {
            "backend": "JAX",
            "model": self.model_name,
            "device": self.device,
            "loaded": self.loaded,
            "has_model": self.model is not None,
            "has_parameters": self.params is not None,
        }