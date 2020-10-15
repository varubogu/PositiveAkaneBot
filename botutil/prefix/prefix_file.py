from .prefix_abstract import PrefixAbstract
import os
import json
import aiofiles

class PrefixFile(PrefixAbstract):

    def __init__(self, prefix = None, prefix_file_path = None):
        super().__init__(prefix)
        self.prefix_file_path = self._coalesce(prefix_file_path, (os.environ.get('PREFIX_FILE_PATH')), "prefix.json")


    async def get(self, guild_id):
        guild_id_str = str(guild_id)
        async with aiofiles.open(self.get_fullpath()) as f:
            contents = await f.read()

        json_data = json.loads(contents)
        prefix = json_data.get(guild_id_str, self.default_prefix)

        return prefix


    async def set(self, guild_id, after_prefix):

        guild_id_str = str(guild_id)

        async with aiofiles.open(self.get_fullpath()) as f:
            contents = await f.read()
            json_data = json.loads(contents)
            before_prefix = json_data.get(guild_id_str, self.default_prefix)
            json_data[guild_id_str] = after_prefix

        async with aiofiles.open(self.get_fullpath(), "w") as f:
            await f.write(json.dumps(json_data))

        return (before_prefix, after_prefix)

    def get_fullpath(self):
        return os.getcwd() + os.sep + self.prefix_file_path