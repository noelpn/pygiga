"""
pygiga.models.model_manager
===========================

Central model manager for PyGiga.

Handles loading, unloading, switching, and managing
multiple AI model backends.
"""

from typing import Any, Dict, List, Optional

from .loader import ModelLoader


class ModelManager:
    """
    Central manager for AI models.
    """

    def __init__(self):
        self._models: Dict[str, Any] = {}
        self._active_model: Optional[str] = None

    def load_model(
        self,
        name: str,
        backend: str,
        model_name: str,
        auto_load: bool = True,
        **kwargs,
    ):
        """
        Load a model and register it.

        Example
        -------
        manager.load_model(
            name="assistant",
            backend="huggingface",
            model_name="gpt2"
        )
        """
        model = ModelLoader.load(
            backend=backend,
            model_name=model_name,
            auto_load=auto_load,
            **kwargs,
        )

        self._models[name] = model

        if self._active_model is None:
            self._active_model = name

        return model

    def add_model(
        self,
        name: str,
        model: Any,
    ) -> None:
        """
        Register an existing model instance.
        """
        self._models[name] = model

        if self._active_model is None:
            self._active_model = name

    def remove_model(
        self,
        name: str,
    ) -> None:
        """
        Remove a model.
        """
        model = self._models.pop(name, None)

        if model and model.is_loaded():
            model.unload()

        if self._active_model == name:
            self._active_model = None

    def get_model(
        self,
        name: str,
    ):
        """
        Return a registered model.
        """
        if name not in self._models:
            raise KeyError(f"Model '{name}' not found.")

        return self._models[name]

    def set_active(
        self,
        name: str,
    ) -> None:
        """
        Set the active model.
        """
        if name not in self._models:
            raise KeyError(f"Model '{name}' not found.")

        self._active_model = name

    def active_model(self):
        """
        Return the active model instance.
        """
        if self._active_model is None:
            return None

        return self._models[self._active_model]

    def active_name(self) -> Optional[str]:
        """
        Return the active model name.
        """
        return self._active_model

    def unload_model(
        self,
        name: str,
    ) -> None:
        """
        Unload a model.
        """
        model = self.get_model(name)

        if model.is_loaded():
            model.unload()

    def unload_all(self) -> None:
        """
        Unload every loaded model.
        """
        for model in self._models.values():
            if model.is_loaded():
                model.unload()

    def generate(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        **kwargs,
    ) -> str:
        """
        Generate text.

        If model_name is omitted,
        the active model is used.
        """
        if model_name is None:
            model = self.active_model()

            if model is None:
                raise RuntimeError("No active model.")

            return model.generate(prompt, **kwargs)

        return self.get_model(model_name).generate(
            prompt,
            **kwargs,
        )

    def predict(
        self,
        inputs: Any,
        model_name: Optional[str] = None,
        **kwargs,
    ):
        """
        Run inference.
        """
        if model_name is None:
            model = self.active_model()

            if model is None:
                raise RuntimeError("No active model.")

            return model.predict(inputs, **kwargs)

        return self.get_model(model_name).predict(
            inputs,
            **kwargs,
        )

    def list_models(self) -> List[str]:
        """
        Return registered model names.
        """
        return list(self._models.keys())

    def clear(self) -> None:
        """
        Unload and remove all models.
        """
        self.unload_all()
        self._models.clear()
        self._active_model = None

    def __len__(self) -> int:
        return len(self._models)

    def __contains__(self, name: str) -> bool:
        return name in self._models

    def __repr__(self) -> str:
        return (
            f"ModelManager("
            f"models={len(self._models)}, "
            f"active={self._active_model})"
        )