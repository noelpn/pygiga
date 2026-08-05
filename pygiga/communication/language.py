"""
pygiga.communication.language
=============================

Language Processor

Provides basic Natural Language Processing (NLP)
utilities for PyGiga.

Author: PyGiga
"""

import re
from typing import List, Dict


class LanguageProcessor:
    """
    Basic language processing.
    """

    def __init__(self):

        self.supported_languages = [
            "en"
        ]

    # --------------------------------------------------
    # Normalize
    # --------------------------------------------------

    def normalize(
        self,
        text: str,
    ) -> str:
        """
        Normalize text.
        """

        text = text.strip()
        text = re.sub(r"\s+", " ", text)

        return text

    # --------------------------------------------------
    # Lowercase
    # --------------------------------------------------

    def lowercase(
        self,
        text: str,
    ) -> str:

        return text.lower()

    # --------------------------------------------------
    # Tokenize
    # --------------------------------------------------

    def tokenize(
        self,
        text: str,
    ) -> List[str]:

        return text.split()

    # --------------------------------------------------
    # Character Count
    # --------------------------------------------------

    def character_count(
        self,
        text: str,
    ) -> int:

        return len(text)

    # --------------------------------------------------
    # Word Count
    # --------------------------------------------------

    def word_count(
        self,
        text: str,
    ) -> int:

        return len(self.tokenize(text))

    # --------------------------------------------------
    # Sentence Count
    # --------------------------------------------------

    def sentence_count(
        self,
        text: str,
    ) -> int:

        return len(
            [
                s
                for s in re.split(
                    r"[.!?]+",
                    text
                )
                if s.strip()
            ]
        )

    # --------------------------------------------------
    # Detect Language
    # --------------------------------------------------

    def detect_language(
        self,
        text: str,
    ) -> str:
        """
        Placeholder language detector.
        """

        return "en"

    # --------------------------------------------------
    # Remove Punctuation
    # --------------------------------------------------

    def remove_punctuation(
        self,
        text: str,
    ) -> str:

        return re.sub(
            r"[^\w\s]",
            "",
            text,
        )

    # --------------------------------------------------
    # Analyze
    # --------------------------------------------------

    def analyze(
        self,
        text: str,
    ) -> Dict:

        normalized = self.normalize(text)

        return {
            "text": normalized,
            "language": self.detect_language(normalized),
            "characters": self.character_count(normalized),
            "words": self.word_count(normalized),
            "sentences": self.sentence_count(normalized),
            "tokens": self.tokenize(normalized),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "processor": "LanguageProcessor",
            "languages": self.supported_languages,
        }