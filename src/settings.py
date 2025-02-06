from typing import Union

from dynaconf import Dynaconf
from pydantic import BaseModel

class SettingsBuilder:
    def __init__(self):
        self.result: Union[BaseModel, None] = None

class Settings:
    @classmethod
    def set(cls) -> BaseModel:
        """
        """

    @classmethod
    def get(cls) -> BaseModel:
        """
        """