import discord
import os
import requests
import time
from discord.ext import tasks
from creds import BOT_TOKEN, SERVER_ID, TEST_ID
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')
guild = client.get_guild(SERVER_ID)


@client.event
async def on_ready():
    print("im alive and working!!(logged in as {0.user})".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For %help"))

'''
@client.event
async def on_member_join(member):
    client.crea
    print()
'''


@client.command()
async def test(ctx):
    await ctx.send("yes chef")


@tasks.loop(seconds=10)
async def myLoop():
    try:
        channel = client.get_channel(TEST_ID)
    except AttributeError:
        print('initialized loop 👍')
    # await channel.send('y0')

myLoop.start()
client.run(BOT_TOKEN)
