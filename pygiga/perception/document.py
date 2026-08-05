"""
pygiga.perception.document
==========================

Document perception module for PyGiga.

Provides utilities for loading, parsing, extracting text,
and processing common document formats.
"""

from pathlib import Path
from typing import Any, Dict


class DocumentPerception:
    """
    Document perception interface.
    """

    SUPPORTED_FORMATS = {
        ".txt",
        ".pdf",
        ".docx",
        ".md",
        ".html",
        ".csv",
        ".json",
    }

    def __init__(self):
        pass

    def load(self, path: str) -> str:
        """
        Load and extract text from a document.
        """
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported document format: {suffix}"
            )

        if suffix == ".txt":
            return path.read_text(encoding="utf-8")

        elif suffix == ".md":
            return path.read_text(encoding="utf-8")

        elif suffix == ".json":
            return path.read_text(encoding="utf-8")

        elif suffix == ".csv":
            return path.read_text(encoding="utf-8")

        elif suffix == ".html":
            try:
                from bs4 import BeautifulSoup
            except ImportError:
                raise ImportError(
                    "beautifulsoup4 is required.\n"
                    "Install using:\n"
                    "pip install beautifulsoup4"
                )

            html = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            return BeautifulSoup(
                html,
                "html.parser",
            ).get_text()

        elif suffix == ".pdf":
            try:
                from pypdf import PdfReader
            except ImportError:
                raise ImportError(
                    "pypdf is required.\n"
                    "Install using:\n"
                    "pip install pypdf"
                )

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

            return text

        elif suffix == ".docx":
            try:
                from docx import Document
            except ImportError:
                raise ImportError(
                    "python-docx is required.\n"
                    "Install using:\n"
                    "pip install python-docx"
                )

            document = Document(path)

            return "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        raise RuntimeError("Unable to read document.")

    def tokenize(
        self,
        text: str,
    ):
        """
        Split text into tokens.
        """
        return text.split()

    def word_count(
        self,
        text: str,
    ) -> int:
        """
        Count words.
        """
        return len(self.tokenize(text))

    def line_count(
        self,
        text: str,
    ) -> int:
        """
        Count lines.
        """
        return len(text.splitlines())

    def summarize(
        self,
        text: str,
        model: Any,
        **kwargs,
    ) -> str:
        """
        Summarize using a supplied model.
        """
        if not hasattr(model, "generate"):
            raise ValueError(
                "Model must implement generate()."
            )

        prompt = (
            "Summarize the following document:\n\n"
            + text
        )

        return model.generate(
            prompt,
            **kwargs,
        )

    def info(
        self,
        path: str,
    ) -> Dict[str, Any]:
        """
        Return document information.
        """
        path = Path(path)

        text = self.load(path)

        return {
            "path": str(path),
            "name": path.name,
            "extension": path.suffix,
            "size_bytes": path.stat().st_size,
            "words": self.word_count(text),
            "lines": self.line_count(text),
        }

    def __repr__(self):
        return (
            f"DocumentPerception("
            f"supported={len(self.SUPPORTED_FORMATS)})"
        )