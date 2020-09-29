from aternosapi import AternosAPI
import os
from discord.ext import commands
from discord import Embed, Color
server = AternosAPI(
  os.environ.get("HEADER_COOKIE"),
  os.environ.get("COOKIE"),
  os.environ.get("ASEC"))
class Server_Command(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
  @commands.group(name='server', invoke_without_command=True)
  async def serverhelp(self, ctx):
    await ctx.send(embed=Embed(title='a!server start: to start the server.\n a!server stop: to stop the server.\n a!server status: to get the status of the server.',color=Color.green()))
  @serverhelp.command(name='start')
  async def start(self, ctx):
    server.StartServer()
    if server.GetStatus() == 'Online':
      print(server.GetStatus())
      await ctx.send(embed=Embed(title=server.GetStatus(), color=Color.green()))
    else:
      while server.GetStatus() != 'Online':
        if server.GetStatus() == 'Online':
          print(server.GetStatus())
          await ctx.send(embed=Embed(title=server.GetStatus(), color=Color.green()))
  @serverhelp.command(name='stop')
  async def stop(self, ctx):
    await ctx.send(embed=Embed(title=server.StopServer(), color=Color.green()))
  @serverhelp.command(name='status')
  async def status(self, ctx):
    await ctx.send(embed=Embed(title=server.GetStatus(), color=Color.green()))


def setup(bot):
  bot.add_cog(Server_Command(bot))
