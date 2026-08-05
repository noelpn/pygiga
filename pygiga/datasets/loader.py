"""
pygiga.datasets.loader
======================

Dataset Loader

Loads datasets from various file formats.

Author: PyGiga
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List


class DatasetLoader:
    """
    Load datasets from disk.
    """

    def __init__(self):

        self.dataset = []

    # --------------------------------------------------
    # Auto Load
    # --------------------------------------------------

    def load(self, path: str):

        extension = Path(path).suffix.lower()

        if extension == ".json":
            return self.load_json(path)

        elif extension == ".jsonl":
            return self.load_jsonl(path)

        elif extension == ".csv":
            return self.load_csv(path)

        elif extension == ".txt":
            return self.load_text(path)

        else:
            raise ValueError(
                f"Unsupported dataset format: {extension}"
            )

    # --------------------------------------------------
    # JSON
    # --------------------------------------------------

    def load_json(self, path: str):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            self.dataset = json.load(file)

        return self.dataset

    # --------------------------------------------------
    # JSONL
    # --------------------------------------------------

    def load_jsonl(self, path: str):

        data = []

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:

                line = line.strip()

                if line:

                    data.append(
                        json.loads(line)
                    )

        self.dataset = data

        return data

    # --------------------------------------------------
    # CSV
    # --------------------------------------------------

    def load_csv(self, path: str):

        data = []

        with open(
            path,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                data.append(row)

        self.dataset = data

        return data

    # --------------------------------------------------
    # TXT
    # --------------------------------------------------

    def load_text(self, path: str):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            lines = [
                line.strip()
                for line in file
                if line.strip()
            ]

        self.dataset = lines

        return lines

    # --------------------------------------------------
    # Save JSON
    # --------------------------------------------------

    def save_json(
        self,
        path: str,
        dataset: List[Any],
    ):

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                dataset,
                file,
                indent=4,
                ensure_ascii=False,
            )

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def size(self):

        return len(self.dataset)

    def empty(self):

        return len(self.dataset) == 0

    def clear(self):

        self.dataset.clear()

    def info(self):

        return {
            "samples": len(self.dataset),
            "type": type(self.dataset).__name__,
        }