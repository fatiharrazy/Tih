import discord
from discord.ext import commands
from replit import db
import random

class NoContext(commands.Cog):
  def __init__(self, client):
    self.client = client

  
  db["nocontext"]

  @commands.command()
  async def nocontext(self, ctx):
    nocontextstuff = db["nocontext"]
    await ctx.send(f"{random.choice(nocontextstuff)}")
  @commands.command()
  async def addnc(self, ctx, imglink : str):
    nc = db["nocontext"]
    nc.append(imglink)
    await ctx.send(f"Image link was succesfully added")

  @nocontext.error
  async def nocontexterror(self, ctx, error):
    print(error)



def setup(client):
  client.add_cog(NoContext(client))