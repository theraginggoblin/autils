"""
This module contains code assisting in implementing the builder design pattern.

Classes:
    BuilderBase
        Base class for creating builder classes.
"""

from abc import ABC, abstractmethod
from typing import Any
import logging

from constants import LOGGER_NAME

LOGGER = logging.getLogger(LOGGER_NAME + "." + __name__)


class BuilderBase(ABC):
    """
    Base class for creating builder classes.
    Contains one abstract method of build that is to be implemented by classes
    that inherit this one.

    Arguments:
        self

    Public methods:
        build
        get
        build_and_get

    Public attributes
        None
    """

    def __init__(self):
        self._result: Any = None

    @abstractmethod
    def build(self) -> None:
        """
        Method to be implemented that should build the desired object and store at self._result

        Calling this more than once will rebuild and overwrite the object at self._result

        Arguments:
            self
        Returns:
            None
        """

    def get(self) -> Any:
        """
        Returns object that at self._result

        Arguments:
            self
        Returns:
            Any
        """
        if self._result is None:
            LOGGER.warning("%s._result is being gotten when it is None", __name__)
        return self._result

    def build_and_get(self) -> Any:
        """
        Calls self.build then self.get to immediately build then return the object.

        Arguments:
            self
        Returns
            Any
        """
        self.build()
        return self.get()
