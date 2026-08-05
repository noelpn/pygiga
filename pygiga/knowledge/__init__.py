"""
pygiga.knowledge
================

Knowledge Management Package

Provides knowledge storage, retrieval, indexing,
embeddings, document management, and knowledge graphs.

Author: PyGiga
"""

from .retrieval import KnowledgeRetrieval
from .indexing import KnowledgeIndexer
from .embeddings import EmbeddingManager
from .documents import DocumentManager
from .graph import KnowledgeGraph

__all__ = [
    "KnowledgeRetrieval",
    "KnowledgeIndexer",
    "EmbeddingManager",
    "DocumentManager",
    "KnowledgeGraph",
]

__version__ = "0.1.0"