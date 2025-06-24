"""
Module containing generic and kind of opinionated classes for managing application
config/settings.

Classes:
    SettingsStore
        Class with class methods that manage a singleton of settings for an application that is
        a Pydantic BaseModel.
    SettingsTransformerBase
        Base class for performing transformations upon a dict where the keys and values are
        known, but further modifications to the dict are required and a passable object
        (instances of this class) is required.
    SettingsDirector
        Mildly opinionated director that builds application settings.
"""

from abc import ABC, abstractmethod
from threading import Lock
from typing import Dict, Any, Type

from dynaconf import Dynaconf
from pydantic import BaseModel

from autils.builder import DirectorBase


class SettingsStore:
    """
    Class with class methods that manage a singleton of settings for an application that is
    a Pydantic BaseModel.
    Includes usage of a threading Lock in case the class is used in a threaded application.
    Opinionated

    Methods:
        put
            Puts/sets the BaseModel singleton.
        get
            Returns the BaseModel singleton.
    """

    _instance: BaseModel | None = None
    _lock: Lock = Lock()

    @classmethod
    def put(cls, settings: BaseModel) -> None:
        """
        Puts/sets the BaseModel singleton.

        Arguments:
            cls
            settings: BaseModel
        Returns:
            BaseModel
        """
        with cls._lock:
            cls._instance = settings

    @classmethod
    def get(cls) -> BaseModel:
        """
        Returns the BaseModel singleton.

        Arguments:
            cls
        Returns:
            BaseModel
        """
        with cls._lock:
            return cls._instance


class SettingsTransformerBase(ABC):
    """
    Base class for performing transformations upon a dict where the keys and values are known,
    but further modifications to the dict are required and a passable object (instances of this
    class) is required.

    Methods:
        transform
            Abstract method where a dict is received, it is modified and returned.
    """

    @abstractmethod
    def transform(self, a_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Abstract method where a dict is received, it is modified and returned.

        Yes, it is known that dicts are mutated in place because they are mutable objects
        but it is more explicit to return the modified dict.

        Arguments:
            a_dict: Dict[str, Any]
        Returns:
            Dict[str, Any]
        """


class SettingsDirector(DirectorBase):
    """
    Mildly opinionated director that builds application settings.

    Methods:
        build
            Uses a Dynaconf instance as a loader, a type of Pydantic BaseModel as an object
            to instantiate, and an optional SettingsTransformerBase to perform transformations.
    """

    def build(
        self,
        loader: Dynaconf,
        model: Type[BaseModel],
        transformer: SettingsTransformerBase = None,
    ) -> BaseModel:
        """
        Uses a Dynaconf instance as a loader, a type of Pydantic BaseModel as an object to
        instantiate, and an optional SettingsTransformerBase to perform transformations.

        loader is used to load settings, then its as_dict method is called.
        transformer performs transformations upon the dict if it was provided.
        model is instantiated with its arguments being the unpacked dict.

        Uses Dynaconf for loading settings because it's just that good, and it lazy loads.
        Uses Pydantic BaseModel for holding the application settings because it will exclude
        any unnecessary settings that Dynaconf loaded, and it provides solid validation.
        Uses SettingsTransformerBase to make any required transformations.

        Arguments:
            loader: Dynaconf
            model: BaseModel
            transformer: SettingsTransformerBase = None
        Returns:
            BaseModel
        """
        # convert to dict with keys as lower case so they match pydantic fields
        settings_dict: Dict[str, Any] = {
            key.lower(): value for key, value in loader.as_dict().items()
        }

        if transformer is not None:
            settings_dict = transformer.transform(settings_dict)

        return model(**settings_dict)


"""
need something to determine files to load
- root path
- files list
need something to determine environment + default environment
- environment
- default environment




what should a class for returning env look like?
looks like dynaconf needs its own builder/director
bit overkill. so could use this, but then it's very opinionated and not flexible
if don't implement here then re-implementing transformation onwards
so back to.. could use a builder/director for just dynaconf per app - starting to like this
need some interface/base class for determining environments
need to work out how to determine what settings_files paths are

so env determiner
object (so not class/static methods)
__init__ may have no args
let's say envs have projects
so multiple args/env vars

map where keys are env+project?
read both args and env vars?

# dynaconf needs to be more flexible
# maybe do dynaconf stuff separately and pass in Dynaconf object?
# root_path should be variable
# settings_files should be variable
# environments should be variable
settings: Dynaconf = Dynaconf(
    root_path = Path(__file__).resolve().parent,
    settings_files = [],
    environments = True,
    default_env = "undefined",
    env = "a_env"
)

"""
