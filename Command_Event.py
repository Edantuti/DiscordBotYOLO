from discord.ext import commands
from discord import Embed, Color

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