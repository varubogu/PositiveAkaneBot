import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

print("hello")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.command()
async def hello(ctx):
    await ctx.send("アカネチャンやで～")

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))