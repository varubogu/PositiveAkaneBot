import os
import abc
from abc import ABCMeta, abstractmethod

class PrefixAbstract(metaclass=ABCMeta):

    def __init__(self, prefix = None):
        self.default_prefix = self._coalesce(prefix, os.environ.get('DEFAULT_PREFIX'), "!")

    @abstractmethod
    async def get(self, guild_id):
        pass

    @abstractmethod
    async def set(self, guild_id, after_prefix):
        pass

    def _coalesce(self, *args):
        for arg in args:
            if arg is not None:
                return arg
        raise ValueError()

