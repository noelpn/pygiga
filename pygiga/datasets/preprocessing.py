"""
pygiga.datasets.preprocessing
=============================

Dataset Preprocessor

Provides dataset preprocessing utilities.

Author: PyGiga
"""

import re
from typing import List, Dict, Any


class DatasetPreprocessor:
    """
    Dataset preprocessing utilities.
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Clean Text
    # --------------------------------------------------

    def clean_text(
        self,
        text: str,
    ) -> str:
        """
        Clean a text string.
        """

        if not isinstance(text, str):
            return ""

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
    # Remove Empty Records
    # --------------------------------------------------

    def remove_empty(
        self,
        dataset: List[Any],
    ) -> List[Any]:

        return [
            item
            for item in dataset
            if item
        ]

    # --------------------------------------------------
    # Normalize Dataset
    # --------------------------------------------------

    def normalize(
        self,
        dataset: List[str],
    ) -> List[str]:

        result = []

        for text in dataset:

            text = self.clean_text(text)

            text = self.lowercase(text)

            result.append(text)

        return result

    # --------------------------------------------------
    # Process Dictionary Dataset
    # --------------------------------------------------

    def process_records(
        self,
        dataset: List[Dict],
        field: str,
    ) -> List[Dict]:

        processed = []

        for record in dataset:

            item = record.copy()

            if field in item:

                text = self.clean_text(
                    str(item[field])
                )

                text = self.lowercase(text)

                item[field] = text

            processed.append(item)

        return processed

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(
        self,
        dataset: List[Any],
    ):

        return {
            "samples": len(dataset)
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "DatasetPreprocessor",
            "version": "0.1.0",
        }