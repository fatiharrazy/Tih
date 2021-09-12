import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client
  @commands.command()
  async def roll(self, ctx, amount=100):
    await ctx.send(f'Rolled {random.randint(1, amount)}!')
  
  @commands.command()
  async def sp(self, ctx, link):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Message sent by {ctx.author.mention}:')
    await ctx.send(f'|| {link} ||')
    
  @commands.command(aliases=['8ball'])
  async def _8ball(self, ctx, *, question):
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

    answer = discord.Embed(
      colour=discord.Color.green()
      )
    answer.add_field(name=f"Question by {ctx.author}", value="{}".format(question), inline=False)
    answer.add_field(name="Answer", value=f"{random.choice(responses)}", inline=False)

    msg = await ctx.send(embed=answer)

  @commands.command()
  async def relationship(self, ctx, member : commands.MemberConverter):

    answer = discord.Embed(
      colour=discord.Color.red()
      )
    answer.add_field(name=f"Relationship Rating", value=f"You are {random.randint(1,100)}% in love with {member.mention}", inline=False)


    msg = await ctx.send(embed=answer)
    
def setup(client):
  client.add_cog(Fun(client))