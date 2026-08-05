"""
pygiga.perception.vision
========================

Vision perception module for PyGiga.

Provides utilities for loading, preprocessing,
analyzing, classifying, detecting objects,
and generating image embeddings.
"""

from pathlib import Path
from typing import Any, Dict

from PIL import Image


class VisionPerception:
    """
    Vision perception interface.
    """

    def __init__(
        self,
        image_size=(224, 224),
    ):
        self.image_size = image_size

    def load(
        self,
        image_path: str,
    ) -> Image.Image:
        """
        Load an image.
        """
        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(path)

        return Image.open(path).convert("RGB")

    def process(
        self,
        image_path: str,
    ) -> Image.Image:
        """
        Load and preprocess an image.
        """
        image = self.load(image_path)

        return image.resize(self.image_size)

    def classify(
        self,
        image_path: str,
        model: Any,
        **kwargs,
    ):
        """
        Classify an image.

        The supplied model must implement predict().
        """
        if not hasattr(model, "predict"):
            raise ValueError(
                "Model must implement predict()."
            )

        image = self.process(image_path)

        return model.predict(image, **kwargs)

    def detect(
        self,
        image_path: str,
        model: Any,
        **kwargs,
    ):
        """
        Perform object detection.

        The supplied model must implement predict().
        """
        if not hasattr(model, "predict"):
            raise ValueError(
                "Model must implement predict()."
            )

        image = self.process(image_path)

        return model.predict(image, **kwargs)

    def segment(
        self,
        image_path: str,
        model: Any,
        **kwargs,
    ):
        """
        Perform image segmentation.

        The supplied model must implement predict().
        """
        if not hasattr(model, "predict"):
            raise ValueError(
                "Model must implement predict()."
            )

        image = self.process(image_path)

        return model.predict(image, **kwargs)

    def embed(
        self,
        image_path: str,
        model: Any,
        **kwargs,
    ):
        """
        Generate image embeddings.

        The supplied model must implement embed().
        """
        if not hasattr(model, "embed"):
            raise ValueError(
                "Model must implement embed()."
            )

        image = self.process(image_path)

        return model.embed(image, **kwargs)

    def describe(
        self,
        image_path: str,
        model: Any,
        **kwargs,
    ) -> str:
        """
        Generate an image caption.

        The supplied model must implement generate().
        """
        if not hasattr(model, "generate"):
            raise ValueError(
                "Model must implement generate()."
            )

        return model.generate(
            image_path,
            **kwargs,
        )

    def info(
        self,
        image_path: str,
    ) -> Dict[str, Any]:
        """
        Return image information.
        """
        image = self.load(image_path)

        return {
            "path": str(Path(image_path)),
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
            "size": image.size,
            "format": image.format,
        }

    def __repr__(self):
        return (
            f"VisionPerception("
            f"image_size={self.image_size})"
        )