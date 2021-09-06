import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client
  @commands.command()
  async def roll(ctx, amount=100):
    await ctx.send(f'Rolled {random.randint(1, amount)}!')

  @commands.command(aliases=['8ball'])
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

def setup(client):
  client.add_cog(Fun(client))