import os
import abc
from abc import ABCMeta, abstractmethod

class PrefixAbstract(metaclass=ABCMeta):

    def __init__(self, prefix:str = None):
        self.default_prefix:str = self._coalesce(prefix, os.environ.get('DEFAULT_PREFIX'), "!")
        self.guild_prefix_dict:dict[int, str] = {}
        self.is_loaded:bool = False


    async def get(self, guild_id:int):
        if (not self.is_loaded):
            await self.load()

        return await self._get(guild_id)


    async def set(self, guild_id:int, after_prefix:str):
        self.is_loaded = False
        before_prefix = await self._get(guild_id)
        await self.save(guild_id, after_prefix)
        return (before_prefix, after_prefix)


    async def load(self):
        result = await self._load()
        self.guild_prefix_dict = result
        self.is_loaded = True
        print('load prefix')



    @abstractmethod
    async def _load(self):
        pass


    @abstractmethod
    async def save(self, guild_id, after_prefix):
        pass



    async def _get(self, guild_id:int):
        return self.guild_prefix_dict.get(guild_id, self.default_prefix)


    def _coalesce(self, *args):
        for arg in args:
            if arg is not None:
                return arg
        raise ValueError()

