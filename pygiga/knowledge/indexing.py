"""
pygiga.knowledge.indexing
=========================

Knowledge Indexer

Indexes knowledge for fast retrieval.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Set


class KnowledgeIndexer:
    """
    Index documents and knowledge.
    """

    def __init__(self):

        self.documents = {}
        self.index = {}

    # --------------------------------------------------
    # Add Document
    # --------------------------------------------------

    def add_document(
        self,
        document_id: str,
        text: str,
    ):

        self.documents[document_id] = {
            "text": text,
            "indexed_at": datetime.utcnow().isoformat(),
        }

        self._index_document(
            document_id,
            text,
        )

    # --------------------------------------------------
    # Internal Indexing
    # --------------------------------------------------

    def _index_document(
        self,
        document_id: str,
        text: str,
    ):

        words = text.lower().split()

        for word in words:

            word = word.strip(".,!?;:\"'()[]{}")

            if not word:
                continue

            if word not in self.index:
                self.index[word] = set()

            self.index[word].add(document_id)

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        query: str,
    ) -> List[Dict]:

        words = query.lower().split()

        results = set()

        for word in words:

            word = word.strip(".,!?;:\"'()[]{}")

            if word in self.index:

                results.update(
                    self.index[word]
                )

        output = []

        for document_id in results:

            output.append({
                "id": document_id,
                "text": self.documents[
                    document_id
                ]["text"],
            })

        return output

    # --------------------------------------------------
    # Remove Document
    # --------------------------------------------------

    def remove_document(
        self,
        document_id: str,
    ):

        if document_id not in self.documents:
            return

        del self.documents[document_id]

        for word in list(self.index.keys()):

            self.index[word].discard(
                document_id
            )

            if not self.index[word]:

                del self.index[word]

    # --------------------------------------------------
    # Vocabulary
    # --------------------------------------------------

    def vocabulary(self):

        return sorted(
            self.index.keys()
        )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "documents": len(
                self.documents
            ),
            "indexed_words": len(
                self.index
            ),
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.documents.clear()

        self.index.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "KnowledgeIndexer",
            "documents": len(
                self.documents
            ),
            "vocabulary": len(
                self.index
            ),
        }