""" """

from pathlib import Path
from threading import Lock
from typing import Dict, Any

from dynaconf import Dynaconf
from pydantic import BaseModel

from autils.builder import DirectorBase


class SettingsStore:
    """ """

    _instance: BaseModel | None = None
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


class SettingsDirector(DirectorBase):
    """ """

    def build(self, settings_model: BaseModel) -> None:
        """
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

        Arguments:
            settings_loader: Dynaconf
            transformer: Transformer
            settings_model: BaseModel
        """



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
        # convert to dict with keys as lower case so they match pydantic fields
        settings_dict: Dict[str, Any] = {key.lower(): value for key, value in settings.as_dict().items()}
        # ---- start transformations
        # use transformation class
        # ---- end transformations
        return settings_model(**settings_dict)


"""
need something to determine files to load
- root path
- files list
need something to determine environment + default environment
- environment
- default environment
"""
