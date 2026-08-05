"""
pygiga.knowledge.retrieval
==========================

Knowledge Retrieval

Retrieves knowledge from indexed documents.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Optional


class KnowledgeRetrieval:
    """
    Retrieve knowledge from a document collection.
    """

    def __init__(self):

        self.documents = {}

    # --------------------------------------------------
    # Add Document
    # --------------------------------------------------

    def add_document(
        self,
        document_id: str,
        text: str,
        metadata: Optional[Dict] = None,
    ):

        if metadata is None:
            metadata = {}

        self.documents[document_id] = {
            "id": document_id,
            "text": text,
            "metadata": metadata,
            "created": datetime.utcnow().isoformat(),
        }

    # --------------------------------------------------
    # Get Document
    # --------------------------------------------------

    def get_document(
        self,
        document_id: str,
    ):

        return self.documents.get(document_id)

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:
        """
        Retrieve the most relevant documents.
        """

        query_words = set(
            query.lower().split()
        )

        results = []

        for document in self.documents.values():

            words = set(
                document["text"].lower().split()
            )

            score = len(
                query_words.intersection(words)
            )

            if score > 0:

                results.append({
                    "document": document,
                    "score": score,
                })

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results[:top_k]

    # --------------------------------------------------
    # Search Metadata
    # --------------------------------------------------

    def search_metadata(
        self,
        key: str,
        value,
    ):

        results = []

        for document in self.documents.values():

            if document["metadata"].get(key) == value:

                results.append(document)

        return results

    # --------------------------------------------------
    # Remove Document
    # --------------------------------------------------

    def remove_document(
        self,
        document_id: str,
    ):

        if document_id in self.documents:

            del self.documents[document_id]

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "documents": len(self.documents)
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
            "module": "KnowledgeRetrieval",
            "documents": len(self.documents),
        }