from discord.ext import commands
import requests
from os import environ
from random import randint
from discord import Activity, ActivityType
from discord import Embed, Color, Member

api = environ.get('API')

class Command(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.group(name='news', invoke_without_command=True)
  async def newshelp(self, ctx):
    await ctx.send('a!news headlines: For the top Headlines\na!news sources: Provides sources')
    
  @newshelp.command(name='headlines')
  async def headlines(self, ctx):
    data = requests.get(url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api).json()
    headlines = data["articles"]
    number = randint(0, len(headlines)-1)
    embed=Embed(title=headlines[number]['title'], url=headlines[number]['url'], color=Color.red())
    url=headlines[number]['urlToImage']
    embed.set_image(url=url)
    await ctx.send(embed=embed)

  @newshelp.command(name='sources')
  async def sources(self, ctx, arg):
    data = requests.get(url="https://newsapi.org/v2/everything?q="+arg+"&apiKey="+api).json()
    sources = data['articles']
    number=randint(0, len(sources)-1)
    embed=Embed(title=sources[number]['title'], url=sources[number]['url'], color=Color.red())
    url=sources[number]['urlToImage']
    embed.set_image(url=url)
    await ctx.send(embed=embed)
  

def setup(bot):
  bot.add_cog(Command(bot))
  