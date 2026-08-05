"""
pygiga.action.filesystem
========================

File System Action Module

Provides file and directory operations.

Author: PyGiga
"""

from pathlib import Path
import shutil
from typing import List


class FileSystemAction:
    """
    File system utility class.
    """

    # --------------------------------------------------
    # Read / Write
    # --------------------------------------------------

    def read(self, path: str, encoding: str = "utf-8") -> str:
        """
        Read a text file.
        """
        return Path(path).read_text(encoding=encoding)

    def write(
        self,
        path: str,
        content: str,
        encoding: str = "utf-8"
    ) -> bool:
        """
        Write to a text file.
        """
        file = Path(path)

        if file.parent:
            file.parent.mkdir(parents=True, exist_ok=True)

        file.write_text(content, encoding=encoding)

        return True

    def append(
        self,
        path: str,
        content: str,
        encoding: str = "utf-8"
    ) -> bool:
        """
        Append text to a file.
        """
        with open(path, "a", encoding=encoding) as f:
            f.write(content)

        return True

    # --------------------------------------------------
    # File Management
    # --------------------------------------------------

    def exists(self, path: str) -> bool:
        return Path(path).exists()

    def delete(self, path: str) -> bool:
        """
        Delete a file.
        """
        file = Path(path)

        if file.exists():
            file.unlink()
            return True

        return False

    def copy(self, source: str, destination: str) -> bool:
        """
        Copy a file.
        """
        shutil.copy2(source, destination)
        return True

    def move(self, source: str, destination: str) -> bool:
        """
        Move a file.
        """
        shutil.move(source, destination)
        return True

    def rename(self, source: str, destination: str) -> bool:
        """
        Rename a file.
        """
        Path(source).rename(destination)
        return True

    # --------------------------------------------------
    # Directory Management
    # --------------------------------------------------

    def create_directory(self, path: str) -> bool:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True

    def remove_directory(self, path: str) -> bool:
        shutil.rmtree(path)
        return True

    def list_directory(self, path: str = ".") -> List[str]:
        """
        List files and folders.
        """
        return [item.name for item in Path(path).iterdir()]

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def size(self, path: str) -> int:
        """
        File size in bytes.
        """
        return Path(path).stat().st_size

    def is_file(self, path: str) -> bool:
        return Path(path).is_file()

    def is_directory(self, path: str) -> bool:
        return Path(path).is_dir()

    def absolute_path(self, path: str) -> str:
        return str(Path(path).resolve())

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def find(self, directory: str, pattern: str = "*") -> List[str]:
        """
        Find files matching a pattern.
        """
        return [
            str(file)
            for file in Path(directory).rglob(pattern)
        ]