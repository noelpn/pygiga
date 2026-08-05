"""
pygiga.models
=============

Unified Model Interface for PyGiga.

Supports multiple AI model backends through a common API.

Available Backends
------------------
- OpenAI
- Gemini
- Ollama
- Hugging Face
- PyTorch
- TensorFlow
- JAX
- Local Models
"""

from .base import BaseModel
from .loader import ModelLoader
from .model_manager import ModelManager
from .registry import ModelRegistry

from .openai import OpenAIModel
from .gemini import GeminiModel
from .ollama import OllamaModel
from .huggingface import HuggingFaceModel
from .pytorch import PyTorchModel
from .tensorflow import TensorFlowModel
from .jax import JAXModel
from .local import LocalModel

__all__ = [
    "BaseModel",
    "ModelLoader",
    "ModelManager",
    "ModelRegistry",
    "OpenAIModel",
    "GeminiModel",
    "OllamaModel",
    "HuggingFaceModel",
    "PyTorchModel",
    "TensorFlowModel",
    "JAXModel",
    "LocalModel",
]

__version__ = "0.1.0"