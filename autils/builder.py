"""
This module contains code assisting in implementing the builder design pattern.

Classes:
    BuilderBase
        Base class for creating builder classes.
    DirectorBase
        Abstract class for building Directors. Contains one abstract method of
        build.
"""

from abc import ABC, abstractmethod
from typing import Any, Self, TypeVar
import logging

from constants import LOGGER_NAME

T = TypeVar('T')

LOGGER = logging.getLogger(LOGGER_NAME + "." + __name__)


class BuilderBase(ABC):
    """
    Base class for creating builder classes.
    Contains one abstract method of build that is to be implemented by classes
    that inherit this one.

    Arguments:
        self

    Methods:
        build
            Abstract method to be implemented that should build the desired object and store
            at self._result
        get
            Returns object that at self._result
        build_and_get
            Calls self.build then self.get to immediately build then return the object
            from self._result.
    """

    def __init__(self):
        self._result: T = None

    @abstractmethod
    def build(self) -> Self:
        """
        Abstract method to be implemented that should build the desired object and store
        at self._result

        Calling this more than once will rebuild and overwrite the object at self._result

        Arguments:
            self
        Returns:
            Self
        """

    def get(self) -> T:
        """
        Returns object that at self._result

        Arguments:
            self
        Returns:
            T
        """
        if self._result is None:
            LOGGER.warning("%s._result is being gotten when it is None", __name__)
        return self._result

    def build_and_get(self) -> T:
        """
        Calls self.build then self.get to immediately build then return the object
        from self._result.

        Arguments:
            self
        Returns
            T
        """
        self.build()
        return self.get()


class DirectorBase(ABC):
    """
    Abstract class for building Directors. Contains one abstract method of
    build.

    The builder argument is optional to enable the creation of basic directors
    that build objects but don't require the use of BuilderBase.

    Arguments:
        self
        builder: BuilderBase | None = None
    Methods:
        set_builder
            Sets the builder used by this director.
            Abstract method that builds the desired object and returns it.
    """

    def __init__(self, builder: BuilderBase | None = None):
        self._builder: BuilderBase | None = builder

    def set_builder(self, builder: BuilderBase | None) -> None:
        """
        Sets the builder used by this director.

        Arguments:
            self
            builder: BuilderBase | None
        Returns:
            None
        """
        self._builder = builder

    @abstractmethod
    def build(self, *args, **kwargs) -> T:
        """
        Abstract method that builds the desired object and returns it.

        Arguments:
            self
            *args
            **kwargs
        Returns:
            T
        """
