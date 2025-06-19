"""
Module containing generic code relating to handling files.

Classes:
    FileUtils
"""

from pathlib import Path
from typing import List


class FileUtils:
    """
    Class of static methods which are file handling utilities.

    Methods:
        get_files_with_extension
            Retrieves all files with a given extension recursively using pathlib.
    """

    @staticmethod
    def get_files_with_extension(directory: str, extension: str) -> List[Path]:
        """
        Retrieves all files with a given extension recursively using pathlib.

        Arguments:
            directory: str
                The starting directory for the search.
            extension: str
                The file extension (e.g., '.txt', '.py').

        Returns:
            List[Path]:
                A list of file paths (Path objects) matching the extension.
        """
        path_obj = Path(directory)
        return list(path_obj.rglob(f"*.{extension}"))


# for unit tests later
# import os
# print(get_files_with_extension(os.getcwd(), "yaml"))
