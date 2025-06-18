""" """

from threading import Lock
from typing import Union

from dynaconf import Dynaconf
from pydantic import BaseModel

from autils.builder import BuilderBase


class SettingsStore:
    """ """

    _instance: Union[BaseModel, None] = None
    _lock: Lock = Lock()

    @classmethod
    def set(cls, config: BaseModel) -> None:
        """ """
        with cls._lock:
            cls._instance = config

    @classmethod
    def get(cls) -> BaseModel:
        """ """
        with cls._lock:
            return cls._instance


class SettingsBuilder(BuilderBase):
    """ """

    def build(self) -> None:
        """ """


"""
need something to determine files to load
- root path
- files list
need something to determine environment + default environment
- environment
- default environment
"""
