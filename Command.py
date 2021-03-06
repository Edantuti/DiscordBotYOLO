from discord.ext import commands
import requests
from os import environ
from random import randint
from sayTime import sayTime
from discord import Embed, Color

s = sayTime()

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
  async def sources(self, ctx, *arg):
    data = requests.get(url="https://newsapi.org/v2/everything?q="+"+".join(arg[:])+"&from="+str(s.sayWeek())+"&to="+str(s.sayToday())+"&sortBy=relevancy&apiKey="+api).json()
    sources = data['articles']
    number=randint(0, len(sources)-1)
    embed=Embed(title=sources[number]['title'], url=sources[number]['url'], color=Color.red())
    url=sources[number]['urlToImage']
    embed.set_image(url=url)
    await ctx.send(embed=embed)
  @newshelp.command(name='search')
  async def search(self, ctx, *arg):
    data = requests.get(url="https://newsapi.org/v2/everything?q="+"+".join(arg[:])+"&from="+str(s.sayWeek())+"&to="+str(s.sayToday())+"&sortBy=relevancy&apiKey="+api).json()
    search = data['articles']
    embed=Embed(title="These are the Search Results:", color=Color.red())
    embed.add_field(name='\n\u200b', value='\n\u200b', inline=False)
    for article in search:
      embed.add_field(name=article['title'], value=article['url'], inline=False)
      embed.add_field(name='\n\u200b', value='\n\u200b', inline=False)
    
    await ctx.send(embed=embed)

  

def setup(bot):
  bot.add_cog(Command(bot))
  