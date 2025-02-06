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
        result
    """

    def __init__(self):
        self.result: Any = None

    @abstractmethod
    def build(self, *args, **kwargs) -> None:
        """
        Method to be implemented that should build the desired object and store at self.result

        Calling this more than once will rebuild and overwrite the object at self.result

        Arguments:
            self
            args
                Any args to be used to build the object stored at self.result
            kwargs
                Any keyword args to be used in building the object stored at self.result
        """

    def get(self) -> Any:
        """

        Arguments:
            self
        Returns:
            Any
                Returns object that at self.result
        """
        if self.result is None:
            LOGGER.warning("%s result is being gotten when it is None", __name__)
        return self.result

    def build_and_get(self, *args, **kwargs) -> Any:
        """
        Calls self.build then self.get to immediately build then return the desired object.

        Arguments:
            self
            args
                Any args to be used to build the object stored at self.result
            kwargs
                Any keyword args to be used in building the object stored at self.result
        """
        self.build(*args, **kwargs)
        return self.get()
