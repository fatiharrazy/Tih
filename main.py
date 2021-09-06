import os
import discord
import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions


bottoken = os.environ['TOKEN']


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Command was not found! try .help to find your command!')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')




client.run(bottoken)