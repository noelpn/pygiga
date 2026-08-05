"""
pygiga.datasets.streaming
=========================

Dataset Streaming

Provides streaming utilities for large datasets.

Author: PyGiga
"""

import csv
import json
from pathlib import Path
from typing import Iterator, Dict, Any


class DatasetStreamer:
    """
    Stream datasets from disk.
    """

    def __init__(self):

        self.records_streamed = 0

    # --------------------------------------------------
    # JSONL Streaming
    # --------------------------------------------------

    def stream_jsonl(
        self,
        path: str,
    ) -> Iterator[Dict[str, Any]]:
        """
        Stream JSONL files.
        """

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                self.records_streamed += 1

                yield json.loads(line)

    # --------------------------------------------------
    # CSV Streaming
    # --------------------------------------------------

    def stream_csv(
        self,
        path: str,
    ) -> Iterator[Dict[str, Any]]:
        """
        Stream CSV files.
        """

        with open(
            path,
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                self.records_streamed += 1

                yield row

    # --------------------------------------------------
    # Text Streaming
    # --------------------------------------------------

    def stream_text(
        self,
        path: str,
    ) -> Iterator[str]:
        """
        Stream text files line by line.
        """

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                self.records_streamed += 1

                yield line

    # --------------------------------------------------
    # Auto Streaming
    # --------------------------------------------------

    def stream(
        self,
        path: str,
    ):
        """
        Automatically select the correct streamer.
        """

        extension = Path(path).suffix.lower()

        if extension == ".jsonl":
            return self.stream_jsonl(path)

        elif extension == ".csv":
            return self.stream_csv(path)

        elif extension == ".txt":
            return self.stream_text(path)

        raise ValueError(
            f"Unsupported streaming format: {extension}"
        )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "records_streamed": self.records_streamed
        }

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.records_streamed = 0

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "DatasetStreamer",
            "supported_formats": [
                "jsonl",
                "csv",
                "txt",
            ],
            "records_streamed": self.records_streamed,
        }