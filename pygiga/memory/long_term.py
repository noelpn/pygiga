"""
pygiga.memory.long_term
=======================

Long Term Memory

Stores persistent knowledge for PyGiga.

Author: PyGiga
"""

from datetime import datetime
from typing import Any, Dict, List


class LongTermMemory:
    """
    Long Term Memory
    """

    def __init__(self):

        self.memory = {}

    # --------------------------------------------------
    # Store
    # --------------------------------------------------

    def store(
        self,
        key: str,
        data: Any,
    ) -> Dict:

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": data,
        }

        self.memory[key] = record

        return record

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def retrieve(
        self,
        key: str,
    ):

        return self.memory.get(key)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(
        self,
        key: str,
        data: Any,
    ):

        if key in self.memory:

            self.memory[key]["data"] = data
            self.memory[key]["timestamp"] = (
                datetime.utcnow().isoformat()
            )

            return self.memory[key]

        return self.store(key, data)

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        key: str,
    ):

        return self.memory.pop(key, None)

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        results = []

        for key, value in self.memory.items():

            if (
                keyword in key.lower()
                or keyword in str(value["data"]).lower()
            ):

                results.append({
                    "key": key,
                    "record": value,
                })

        return results

    # --------------------------------------------------
    # Keys
    # --------------------------------------------------

    def keys(self):

        return list(self.memory.keys())

    # --------------------------------------------------
    # Values
    # --------------------------------------------------

    def values(self):

        return list(self.memory.values())

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.memory.clear()

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "records": len(self.memory),
        }

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "LongTermMemory",
            "records": len(self.memory),
        }