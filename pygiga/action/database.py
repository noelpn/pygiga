"""
pygiga.action.database
======================

Database Action Module

Provides database operations using SQLite.

Author: PyGiga
"""

import sqlite3
from typing import Any, Dict, List, Optional


class DatabaseAction:
    """
    Database utility class.
    """

    def __init__(self, database: str = "pygiga.db"):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def execute(
        self,
        query: str,
        parameters: tuple = ()
    ) -> None:
        """
        Execute an SQL query.
        """
        self.cursor.execute(query, parameters)
        self.connection.commit()

    def fetch_one(
        self,
        query: str,
        parameters: tuple = ()
    ) -> Optional[Dict[str, Any]]:
        """
        Return one record.
        """
        self.cursor.execute(query, parameters)
        row = self.cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    def fetch_all(
        self,
        query: str,
        parameters: tuple = ()
    ) -> List[Dict[str, Any]]:
        """
        Return all matching records.
        """
        self.cursor.execute(query, parameters)
        rows = self.cursor.fetchall()

        return [dict(row) for row in rows]

    def insert(
        self,
        table: str,
        values: Dict[str, Any]
    ) -> None:

        columns = ", ".join(values.keys())
        placeholders = ", ".join(["?"] * len(values))

        sql = (
            f"INSERT INTO {table} "
            f"({columns}) "
            f"VALUES ({placeholders})"
        )

        self.cursor.execute(sql, tuple(values.values()))
        self.connection.commit()

    def update(
        self,
        table: str,
        values: Dict[str, Any],
        where: str,
        parameters: tuple = ()
    ) -> None:

        assignments = ", ".join(
            [f"{column}=?" for column in values]
        )

        sql = (
            f"UPDATE {table} "
            f"SET {assignments} "
            f"WHERE {where}"
        )

        self.cursor.execute(
            sql,
            tuple(values.values()) + parameters
        )

        self.connection.commit()

    def delete(
        self,
        table: str,
        where: str,
        parameters: tuple = ()
    ) -> None:

        sql = (
            f"DELETE FROM {table} "
            f"WHERE {where}"
        )

        self.cursor.execute(sql, parameters)
        self.connection.commit()

    def tables(self) -> List[str]:
        """
        List all tables.
        """
        self.cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table';"
        )

        return [
            row[0]
            for row in self.cursor.fetchall()
        ]

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()