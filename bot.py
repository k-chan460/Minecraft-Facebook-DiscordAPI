import discord
from discord.ext.commands import Bot
from discord.ext import commands
from mcstatus import MinecraftServer
import threading

Client = discord.Client()
bot_prefix = "?"
client = commands.Bot(command_prefix = bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")


@client.command(pass_context = True)
async def online(ctx):
    await client.say("The town members currently online are:")

client.run("MzUxOTQwMjAxMDc5MTExNjgx.DIZ6qA.bRu1dAMTBxHy913DhzBhxX-Z3iQ")
