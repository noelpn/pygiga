# pygiga/safety/sandbox.py

import multiprocessing
import traceback
from dataclasses import dataclass


@dataclass
class SandboxResult:
    success: bool
    output: str = ""
    error: str = ""


class Sandbox:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def _runner(self, code, queue):
        try:
            namespace = {
                "__builtins__": {
                    "print": print,
                    "len": len,
                    "range": range,
                    "str": str,
                    "int": int,
                    "float": float,
                    "list": list,
                    "dict": dict,
                    "set": set,
                    "tuple": tuple,
                    "bool": bool,
                    "enumerate": enumerate,
                    "zip": zip,
                }
            }

            exec(code, namespace)

            queue.put(SandboxResult(
                success=True,
                output="Execution completed."
            ))

        except Exception:
            queue.put(
                SandboxResult(
                    success=False,
                    error=traceback.format_exc()
                )
            )

    def execute(self, code):
        queue = multiprocessing.Queue()

        process = multiprocessing.Process(
            target=self._runner,
            args=(code, queue)
        )

        process.start()
        process.join(self.timeout)

        if process.is_alive():
            process.terminate()
            process.join()

            return SandboxResult(
                success=False,
                error="Execution timed out."
            )

        if not queue.empty():
            return queue.get()

        return SandboxResult(
            success=False,
            error="Unknown sandbox error."
        )