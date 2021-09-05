import os
import discord
import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions


bottoken = os.environ['TOKEN']


client = commands.Bot(command_prefix = 'tih!')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def roll(ctx, amount=100):
  await ctx.send(f'Rolled {random.randint(1, amount)}!')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
'It is Certain.',
'It is decidedly so.',
'Without a doubt.',
'Yes definitely.',
'You may rely on it.',
'As I see it, yes.',
'Most likely.',
'Outlook good.',
'Yes.',
'Signs point to yes.',
'Reply hazy, try again.',
'Ask again later.',
'Better not tell you now.',
'Cannot predict now.',
'Concentrate and ask again.',
'Dont count on it.',
'My reply is no.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful.']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member.mention} has been kicked for: "{reason}".')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'User {member.mention} has been banned for: "{reason}".')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(":x: You don't have permission to kick members.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(":x: You don't have permission to ban members.")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(":x: You don't have permission to purge messages.")

client.run(bottoken)