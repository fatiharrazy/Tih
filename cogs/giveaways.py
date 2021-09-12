import discord
import datetime
import time
import asyncio
import random
from discord.ext.commands import MissingPermissions
from discord.ext.commands import MissingRequiredArgument

from discord.ext import commands
from discord import Embed

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx, time: int, *, prize):
        giveawayembed = discord.Embed(
            title="🎉 New Giveaway! 🎉",
            colour=discord.Color.green()
            )

        giveawayembed.add_field(name="Prize", value="{}".format(prize), inline=False)
        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
        giveawayembed.add_field(name="Ends in", value="{}s".format(time))

        msg = await ctx.send(embed=giveawayembed)

        await msg.add_reaction("🎉")

        await asyncio.sleep(time)

        msg = await msg.channel.fetch_message(msg.id)
        winner = None
        
        for reaction in msg.reactions:
            if reaction.emoji == "🎉":
                users = await reaction.users().flatten()
                users.remove(self.client.user)
                winner = random.choice(users)

        if winner is not None:
            endembed = discord.Embed(
                title="Giveaway ended!",
                description="Prize: {}\nWinner: {}".format(prize, winner))
            endembed.set_footer(text=f"Please contact {ctx.author} in the next 24 hours to claim")
            await msg.edit(embed=endembed)
            await ctx.send(f"Congratulations! {winner.mention} for winning the giveaway!")
    @giveaway.error
    async def giveaway_error(self, ctx, error):
      if isinstance(error, MissingRequiredArgument):
        await ctx.send(f'Missing lines! Please use t.giveaways <time (in seconds)> <Prize>')
      else:
        await ctx.send(f'Please use t.giveaways <time (in seconds)> <Prize>')

def setup(client):
    client.add_cog(Giveaway(client))