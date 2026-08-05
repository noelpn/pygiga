"""
pygiga.evaluation.reporting
===========================

Report Generator

Creates evaluation reports.

Author: PyGiga
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


class ReportGenerator:
    """
    Generate evaluation reports.
    """

    def __init__(self):

        self.reports = []

    # --------------------------------------------------
    # Create Report
    # --------------------------------------------------

    def create(
        self,
        title: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Create a report.
        """

        report = {
            "title": title,
            "timestamp": datetime.utcnow().isoformat(),
            "data": data,
        }

        self.reports.append(report)

        return report

    # --------------------------------------------------
    # JSON
    # --------------------------------------------------

    def to_json(
        self,
        report: Dict[str, Any],
    ) -> str:
        """
        Convert report to JSON.
        """

        return json.dumps(
            report,
            indent=4,
            ensure_ascii=False,
        )

    # --------------------------------------------------
    # Text
    # --------------------------------------------------

    def to_text(
        self,
        report: Dict[str, Any],
    ) -> str:
        """
        Convert report to plain text.
        """

        lines = []

        lines.append("=" * 50)
        lines.append(report["title"])
        lines.append("=" * 50)

        lines.append(
            f"Generated : {report['timestamp']}"
        )

        lines.append("")

        for key, value in report["data"].items():

            lines.append(
                f"{key}: {value}"
            )

        return "\n".join(lines)

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save_json(
        self,
        path: str,
        report: Dict[str, Any],
    ):

        Path(path).write_text(
            self.to_json(report),
            encoding="utf-8",
        )

    def save_text(
        self,
        path: str,
        report: Dict[str, Any],
    ):

        Path(path).write_text(
            self.to_text(report),
            encoding="utf-8",
        )

    # --------------------------------------------------
    # Reports
    # --------------------------------------------------

    def latest(self):

        if not self.reports:
            return None

        return self.reports[-1]

    def history(self):

        return self.reports

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        return {
            "reports_generated": len(
                self.reports
            )
        }

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.reports.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "ReportGenerator",
            "reports": len(self.reports),
        }