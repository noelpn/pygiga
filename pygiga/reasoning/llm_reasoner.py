"""
pygiga.reasoning.llm_reasoner
=============================

LLM Reasoning Module

Provides a generic interface for reasoning with
Large Language Models (LLMs).
"""

from typing import Any, Optional


class LLMReasoner:
    """
    Generic LLM reasoning wrapper.
    """

    def __init__(self, model: Optional[Any] = None):
        self.model = model

    def set_model(self, model: Any) -> None:
        """
        Set the language model.
        """
        self.model = model

    def reason(self, prompt: str, **kwargs) -> str:
        """
        Perform reasoning using the attached model.

        The model is expected to implement either:
            - generate(prompt, **kwargs)
            - __call__(prompt, **kwargs)
        """
        if self.model is None:
            raise RuntimeError("No language model has been assigned.")

        if hasattr(self.model, "generate"):
            return self.model.generate(prompt, **kwargs)

        if callable(self.model):
            return self.model(prompt, **kwargs)

        raise TypeError(
            "The provided model does not support reasoning."
        )

    def available(self) -> bool:
        """
        Return whether a model is available.
        """
        return self.model is not None

    def clear(self):
        """
        Remove the attached model.
        """
        self.model = None

    def __repr__(self):
        status = "loaded" if self.model else "none"
        return f"LLMReasoner(model={status})"