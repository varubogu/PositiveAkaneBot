import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from botutil.prefix import PrefixFile

load_dotenv()

prefix_manager = PrefixFile()

async def prefix_load(bot, message):
    prefix = await prefix_manager.get(message.guild.id)
    return commands.when_mentioned_or(prefix)(bot, message)


bot = commands.Bot(command_prefix=prefix_load)

@bot.event
async def ready():
    print('init ok')

@bot.command()
async def hello(ctx):
    await ctx.send("アカネチャンやで～")


@bot.command()
async def prefix(ctx, prefix = None):

    if ctx.author.bot: return

    if prefix is None:
        now_prefix = await prefix_manager.get(ctx.guild.id)
        await ctx.send('アカネチャン呼び出す時の命令は "{0}" やで'.format(now_prefix))
    else:
        result = await prefix_manager.set(ctx.guild.id, prefix)
        await ctx.send('アカネチャン呼び出す時の命令が "{0}" から "{1}" に変わったで～'.format(result[0], result[1]))

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))