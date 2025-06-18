from dynaconf import Dynaconf
from pprint import pprint

settings = Dynaconf(
    envvar_prefix="DYNACONF",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=["settings.toml"],  # Load files in the given order.
)

pprint(settings.to_dict())
