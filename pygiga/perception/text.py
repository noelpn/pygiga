"""
pygiga.perception.text
======================

Text perception module for PyGiga.

Provides utilities for processing, analyzing, tokenizing,
cleaning, and embedding text.
"""

import re
from typing import Any, Dict, List


class TextPerception:
    """
    Text perception interface.
    """

    def __init__(self):
        pass

    def process(
        self,
        text: str,
        lowercase: bool = True,
        remove_extra_spaces: bool = True,
    ) -> str:
        """
        Basic text preprocessing.
        """
        if lowercase:
            text = text.lower()

        if remove_extra_spaces:
            text = re.sub(r"\s+", " ", text).strip()

        return text

    def tokenize(
        self,
        text: str,
    ) -> List[str]:
        """
        Split text into tokens.
        """
        return self.process(text).split()

    def sentences(
        self,
        text: str,
    ) -> List[str]:
        """
        Split text into sentences.
        """
        text = text.strip()

        if not text:
            return []

        return re.split(r"(?<=[.!?])\s+", text)

    def word_count(
        self,
        text: str,
    ) -> int:
        """
        Count words.
        """
        return len(self.tokenize(text))

    def character_count(
        self,
        text: str,
    ) -> int:
        """
        Count characters.
        """
        return len(text)

    def language(
        self,
        text: str,
    ) -> str:
        """
        Detect language.
        """
        try:
            from langdetect import detect

            return detect(text)

        except ImportError:
            raise ImportError(
                "langdetect is required.\n"
                "Install using:\n"
                "pip install langdetect"
            )

    def keywords(
        self,
        text: str,
        top_k: int = 10,
    ) -> List[str]:
        """
        Extract simple keywords based on frequency.
        """
        words = self.tokenize(text)

        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        sorted_words = sorted(
            frequency.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            word
            for word, _ in sorted_words[:top_k]
        ]

    def embed(
        self,
        text: str,
        model: Any,
        **kwargs,
    ):
        """
        Generate embeddings using a supplied model.
        """
        if not hasattr(model, "embed"):
            raise ValueError(
                "Model must implement embed()."
            )

        return model.embed(text, **kwargs)

    def summarize(
        self,
        text: str,
        model: Any,
        **kwargs,
    ) -> str:
        """
        Summarize text using a supplied model.
        """
        if not hasattr(model, "generate"):
            raise ValueError(
                "Model must implement generate()."
            )

        prompt = (
            "Summarize the following text:\n\n"
            + text
        )

        return model.generate(prompt, **kwargs)

    def info(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """
        Return text statistics.
        """
        return {
            "characters": self.character_count(text),
            "words": self.word_count(text),
            "sentences": len(self.sentences(text)),
            "language": self.language(text),
        }

    def __repr__(self):
        return "TextPerception()"