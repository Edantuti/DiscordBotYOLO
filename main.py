#Adding all the necessary functions from the packages
from keep_alive import keep_alive
from aternosapi import AternosAPI
from random2 import randint
import requests
import threading
import time
from discord.ext import commands
from discord import CustomActivity, ActivityType, Activity
from discord import Guild
from discord import Embed, Color
import os

#Get constants from .env file
headers_cookie = os.environ.get("HEADER_COOKIE")
cookie = os.environ.get("COOKIE")
ASEC = os.environ.get("ASEC")
api = os.environ.get("API")

#aternos server object
server = AternosAPI(headers_cookie, cookie, ASEC)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('a!'))
#removing the default help function

bot.remove_command('help')

#Gives response on the console when the bot is ready

#just to check whether the bot is good
@bot.command()
async def hello(ctx):
    embed=Embed(title="hello", color=Color.green())
    await ctx.send(embed=embed)

#Command that actually starts the server
@bot.command()
async def start(ctx):
    server.StartServer()
    starter.start()
    if server.GetStatus() == 'Online':
        embed = Embed(title="Bhau server online hai", color=Color.blue())
        await ctx.send(embed=embed)
    elif server.GetStatus() == 'Offline':
      server.StartServer()
      time.sleep(90)
    else:
        b = True
        time.sleep(30)
        while b:
          time.sleep(30)
          if server.GetStatus() == 'Online':
            embed = Embed(title="Bhau server online hai", color=Color.blue())
            await ctx.send(embed=embed)

#Command that stops the server
@bot.command()
async def stop(ctx):
    embed=Embed(title=server.StopServer(), color=Color.blue())
    await ctx.send(embed=embed)
    await ctx.send(str(ctx.author.mention))

#Command that gives of the server
@bot.command()
async def status(ctx):
    embed=Embed(title=server.GetStatus(), color=Color.blue())
    await ctx.send(embed=embed)
    await ctx.send(ctx.author.mention)

#Command which provides all the commands that are present in the code
@bot.command()
async def help(ctx):
    embed=Embed(title='Helps/commands of the '+(bot.user.name), description="This Bot is made By Edantuti.",color=Color.dark_blue())
    embed.set_author(name="Developer:Edan Solomon Tuti", url='https://github.com/Edantuti/DiscordBotYOLO')
    embed.add_field(name='News:', value='The command for news:\na!headlines-To show the top headlines in India.\na!sources <query>-To get the news for specific topic.', inline=True)
    embed.add_field(name='Aternos Minecraft:', value='The commands: \na!start-To start the server.\na!stop-To stop the server.\na!status-To get the status of the server.', inline=True)
    await ctx.send(embed=embed)

starter = threading.Thread(target=start, args=('a!'))

keep_alive()
bot.load_extension('Command')
bot.load_extension('Command_Event')
token = os.environ.get("DISCORD_TOKEN_SECRET")

bot.run(token)

