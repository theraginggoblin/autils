""" """

from pathlib import Path
from typing import List


class FileUtils:
    """ """

    @staticmethod
    def get_files_with_extension(directory: str, extension: str) -> List[Path]:
        """
        Retrieves all files with a given extension recursively using pathlib.

        Args:
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
