"""
pygiga.knowledge.graph
======================

Knowledge Graph

Stores entities and relationships.

Author: PyGiga
"""

from datetime import datetime
from typing import Dict, List, Optional


class KnowledgeGraph:
    """
    Simple knowledge graph.
    """

    def __init__(self):

        self.nodes = {}
        self.edges = []

    # --------------------------------------------------
    # Add Node
    # --------------------------------------------------

    def add_node(
        self,
        node_id: str,
        data: Optional[Dict] = None,
    ):

        if data is None:
            data = {}

        self.nodes[node_id] = {
            "id": node_id,
            "data": data,
            "created": datetime.utcnow().isoformat(),
        }

        return self.nodes[node_id]

    # --------------------------------------------------
    # Get Node
    # --------------------------------------------------

    def get_node(
        self,
        node_id: str,
    ):

        return self.nodes.get(node_id)

    # --------------------------------------------------
    # Remove Node
    # --------------------------------------------------

    def remove_node(
        self,
        node_id: str,
    ):

        if node_id not in self.nodes:
            return False

        del self.nodes[node_id]

        self.edges = [
            edge
            for edge in self.edges
            if edge["source"] != node_id
            and edge["target"] != node_id
        ]

        return True

    # --------------------------------------------------
    # Add Edge
    # --------------------------------------------------

    def add_edge(
        self,
        source: str,
        target: str,
        relation: str,
    ):

        if source not in self.nodes:
            raise ValueError(f"Unknown node: {source}")

        if target not in self.nodes:
            raise ValueError(f"Unknown node: {target}")

        edge = {
            "source": source,
            "target": target,
            "relation": relation,
            "created": datetime.utcnow().isoformat(),
        }

        self.edges.append(edge)

        return edge

    # --------------------------------------------------
    # Remove Edge
    # --------------------------------------------------

    def remove_edge(
        self,
        source: str,
        target: str,
        relation: str,
    ):

        self.edges = [
            edge
            for edge in self.edges
            if not (
                edge["source"] == source
                and edge["target"] == target
                and edge["relation"] == relation
            )
        ]

    # --------------------------------------------------
    # Neighbors
    # --------------------------------------------------

    def neighbors(
        self,
        node_id: str,
    ) -> List[Dict]:

        result = []

        for edge in self.edges:

            if edge["source"] == node_id:

                result.append(
                    self.nodes[edge["target"]]
                )

        return result

    # --------------------------------------------------
    # Find Relations
    # --------------------------------------------------

    def relations(
        self,
        node_id: str,
    ) -> List[Dict]:

        return [
            edge
            for edge in self.edges
            if edge["source"] == node_id
            or edge["target"] == node_id
        ]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ):

        keyword = keyword.lower()

        results = []

        for node in self.nodes.values():

            if keyword in str(node).lower():

                results.append(node)

        return results

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges),
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.nodes.clear()
        self.edges.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "KnowledgeGraph",
            "nodes": len(self.nodes),
            "edges": len(self.edges),
        }