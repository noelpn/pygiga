"""
pygiga.knowledge.documents
==========================

Document Manager

Manages knowledge documents.

Author: PyGiga
"""

from pathlib import Path
from datetime import datetime
from typing import List, Dict


class DocumentManager:
    """
    Manage documents used by PyGiga.
    """

    def __init__(self):

        self.documents = []

    # --------------------------------------------------
    # Add Document
    # --------------------------------------------------

    def add(
        self,
        title: str,
        content: str,
        source: str = "local",
    ) -> Dict:

        document = {
            "id": len(self.documents) + 1,
            "title": title,
            "content": content,
            "source": source,
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.documents.append(document)

        return document

    # --------------------------------------------------
    # Load Text File
    # --------------------------------------------------

    def load_text(
        self,
        path: str,
    ) -> Dict:

        file = Path(path)

        text = file.read_text(
            encoding="utf-8"
        )

        return self.add(
            title=file.name,
            content=text,
            source=str(file),
        )

    # --------------------------------------------------
    # Save Text File
    # --------------------------------------------------

    def save_text(
        self,
        path: str,
        content: str,
    ):

        Path(path).write_text(
            content,
            encoding="utf-8",
        )

    # --------------------------------------------------
    # Get Document
    # --------------------------------------------------

    def get(
        self,
        document_id: int,
    ):

        for document in self.documents:

            if document["id"] == document_id:

                return document

        return None

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        return [
            document
            for document in self.documents
            if keyword in document["title"].lower()
            or keyword in document["content"].lower()
        ]

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def remove(
        self,
        document_id: int,
    ):

        self.documents = [
            document
            for document in self.documents
            if document["id"] != document_id
        ]

    # --------------------------------------------------
    # List Documents
    # --------------------------------------------------

    def list(self):

        return self.documents

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        total_characters = sum(
            len(document["content"])
            for document in self.documents
        )

        return {
            "documents": len(self.documents),
            "characters": total_characters,
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.documents.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "DocumentManager",
            "documents": len(self.documents),
        }