"""
pygiga.evaluation.benchmark
===========================

Benchmark Module

Runs benchmarks for PyGiga components.

Author: PyGiga
"""

import time
from typing import Any, Callable, Dict, List


class Benchmark:
    """
    Benchmark execution utilities.
    """

    def __init__(self):

        self.results = []

    # --------------------------------------------------
    # Benchmark Function
    # --------------------------------------------------

    def run(
        self,
        name: str,
        function: Callable,
        *args,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Benchmark a Python function.
        """

        start = time.perf_counter()

        output = function(*args, **kwargs)

        end = time.perf_counter()

        result = {
            "name": name,
            "execution_time": end - start,
            "success": True,
            "output": output,
        }

        self.results.append(result)

        return result

    # --------------------------------------------------
    # Benchmark Multiple
    # --------------------------------------------------

    def run_many(
        self,
        benchmarks: List[Dict]
    ) -> List[Dict]:
        """
        Run multiple benchmarks.
        """

        outputs = []

        for benchmark in benchmarks:

            outputs.append(
                self.run(
                    benchmark["name"],
                    benchmark["function"],
                    *benchmark.get("args", ()),
                    **benchmark.get("kwargs", {})
                )
            )

        return outputs

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    def history(self):

        return self.results

    def latest(self):

        if not self.results:
            return None

        return self.results[-1]

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self):

        if not self.results:

            return {
                "benchmarks": 0,
                "average_time": 0,
            }

        average = sum(
            r["execution_time"]
            for r in self.results
        ) / len(self.results)

        return {
            "benchmarks": len(self.results),
            "average_time": average,
        }

    # --------------------------------------------------
    # Fastest
    # --------------------------------------------------

    def fastest(self):

        if not self.results:
            return None

        return min(
            self.results,
            key=lambda r: r["execution_time"]
        )

    # --------------------------------------------------
    # Slowest
    # --------------------------------------------------

    def slowest(self):

        if not self.results:
            return None

        return max(
            self.results,
            key=lambda r: r["execution_time"]
        )

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self.results.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "module": "Benchmark",
            "runs": len(self.results),
        }