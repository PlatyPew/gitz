import json
import os
from . import util

PREFIX = 'GITZ_'
CONFIG_FILE = '.gitz.json'


class Env:
    DEFAULTS = {
        'PROTECTED_BRANCHES': 'master:develop',
        'PROTECTED_REMOTES': 'upstream',
        'FRESH_BRANCHES': 'develop:master',
    }

    def __getattr__(self, key):
        return lambda: self.get(key)

    def get(self, key):
        key = key.upper()
        default = self.DEFAULTS.get(key)
        if default is None:
            raise KeyError(key)

        value = os.environ.get(PREFIX + key)
        if value is not None:
            return value

        root = util.find_git_root()
        if not (root and (root / CONFIG_FILE).exists()):
            return default

        config = json.load(open(str(root / CONFIG_FILE)))
        value = config.get(key, config.get(key.lower()))
        if value is None:
            value = default

        return value.split(':')


ENV = Env()
