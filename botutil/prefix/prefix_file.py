import os
import json
import aiofiles

from .prefix_abstract import PrefixAbstract

class PrefixFile(PrefixAbstract):

    def __init__(self, prefix = None, prefix_file_path = None):
        super().__init__(prefix)
        self.prefix_file_path = (prefix_file_path or os.environ.get('PREFIX_FILE_PATH') or "prefix.json")


    async def _load(self):
        async with aiofiles.open(self.get_fullpath()) as f:
            contents = await f.read()

        json_data = json.loads(contents)

        result_prefix_dict:dict[int, str] = {}
        for key in json_data.keys():
            result_prefix_dict[int(key)] = json_data[key]

        return result_prefix_dict


    async def save(self, guild_id, after_prefix):

        guild_id_str = str(guild_id)

        async with aiofiles.open(self.get_fullpath()) as f:
            contents = await f.read()

        json_data = json.loads(contents)
        json_data[guild_id_str] = after_prefix

        async with aiofiles.open(self.get_fullpath(), "w") as f:
            await f.write(json.dumps(json_data))


    def get_fullpath(self) -> str:
        return os.getcwd() + os.sep + self.prefix_file_path