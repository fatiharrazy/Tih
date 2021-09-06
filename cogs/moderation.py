import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord.ext.commands import MissingRequiredArgument

class Moderation(commands.Cog): 
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Deleted {amount} messages. ')

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member.mention} has been kicked for: "{reason}".')

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member.mention} has been banned for: "{reason}".')

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}.')
        return


  @kick.error
  async def kick_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
          await ctx.send(":x: You don't have permission to kick members.")
      elif isinstance(error, MissingRequiredArgument):
        await ctx.send('Please specify a member.')

  @ban.error
  async def ban_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
          await ctx.send(":x: You don't have permission to ban members.")
      elif isinstance(error, MissingRequiredArgument):
        await ctx.send('Please specify a member.')

  @clear.error
  async def clear_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
          await ctx.send(":x: You don't have permission to purge messages.")
      elif isinstance(error, MissingRequiredArgument):
        await ctx.send('Please specify how many messages you want to delete.')
  @unban.error
  async def unban_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
          await ctx.send(":x: You don't have permission to unban members.")
      elif isinstance(error, MissingRequiredArgument):
        await ctx.send('Please specify the User ID (ex. John#0001)')


def setup(client):
  client.add_cog(Moderation(client))