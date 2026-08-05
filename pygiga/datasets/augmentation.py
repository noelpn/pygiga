"""
pygiga.datasets.augmentation
============================

Dataset Augmentation

Provides simple dataset augmentation utilities.

Author: PyGiga
"""

import random
from typing import List, Dict, Any


class DatasetAugmentation:
    """
    Dataset augmentation utilities.
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Duplicate Samples
    # --------------------------------------------------

    def duplicate(
        self,
        dataset: List[Any],
        times: int = 2,
    ) -> List[Any]:
        """
        Duplicate dataset entries.
        """

        augmented = []

        for item in dataset:
            for _ in range(times):
                augmented.append(item)

        return augmented

    # --------------------------------------------------
    # Shuffle
    # --------------------------------------------------

    def shuffle(
        self,
        dataset: List[Any],
    ) -> List[Any]:
        """
        Shuffle dataset.
        """

        data = dataset.copy()

        random.shuffle(data)

        return data

    # --------------------------------------------------
    # Sample
    # --------------------------------------------------

    def sample(
        self,
        dataset: List[Any],
        size: int,
    ) -> List[Any]:
        """
        Random sample.
        """

        return random.sample(
            dataset,
            min(size, len(dataset))
        )

    # --------------------------------------------------
    # Merge
    # --------------------------------------------------

    def merge(
        self,
        dataset1: List[Any],
        dataset2: List[Any],
    ) -> List[Any]:
        """
        Merge two datasets.
        """

        return dataset1 + dataset2

    # --------------------------------------------------
    # Remove Duplicates
    # --------------------------------------------------

    def remove_duplicates(
        self,
        dataset: List[Dict],
    ) -> List[Dict]:
        """
        Remove duplicate records.
        """

        seen = set()

        result = []

        for item in dataset:

            key = str(item)

            if key not in seen:

                seen.add(key)

                result.append(item)

        return result

    # --------------------------------------------------
    # Train/Test Split
    # --------------------------------------------------

    def split(
        self,
        dataset: List[Any],
        train_ratio: float = 0.8,
    ):

        data = self.shuffle(dataset)

        index = int(
            len(data) * train_ratio
        )

        train = data[:index]

        test = data[index:]

        return train, test

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
            "module": "DatasetAugmentation",
            "version": "0.1.0",
        }