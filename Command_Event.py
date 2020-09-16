from discord.ext import commands
import requests
from os import environ
from random import randint
from discord import Activity, ActivityType
from discord import Embed, Color, Member

class Command_Event(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("ready")

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    print(str(error))
    embed=Embed(title="Wrong Command", color=Color.dark_teal())
    await ctx.send(embed=embed)
      
def setup(bot):
  bot.add_cog(Command_Event(bot))