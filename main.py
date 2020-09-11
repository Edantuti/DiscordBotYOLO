#Adding all the necessary functions from the packages
from keep_alive import keep_alive
from aternosapi import AternosAPI
from random2 import randint
import requests
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
@bot.event
async def on_ready():
    print("Logged in as"+str(bot.user.name)+str(bot.user.id))
    await bot.change_presence(activity=Activity(name="a!help", type=ActivityType.playing))

#Error heading
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=Embed(title="Wrong Command", color=Color.dark_red())
        await ctx.send(embed=embed)
    else:
        embed=Embed(title="Wrong Command", color=Color.dark_teal())
        await ctx.send(embed=embed)

#just to check whether the bot is good
@bot.command()
async def hello(ctx):
    await bot.change_presence(activity=CustomActivity(name="Hi!", type=ActivityType.playing))
    embed=Embed(title="hello", color=Color.green())
    await ctx.send(embed=embed)

#Command that actually starts the server
@bot.command()
async def start(ctx):
    await bot.change_presence(activity=CustomActivity(name="Starting the Server", type=ActivityType.playing))
    server.StartServer()
    if server.GetStatus() == 'Online':
        embed = Embed(title="Bhau server online hai", color=Color.blue())
        await ctx.send(embed=embed)
    else:
        b = True
        while b:
            if server.GetStatus() == 'Online':
                embed = Embed(title="Bhau server online hai", color=Color.blue())
                await ctx.send(embed=embed)

#Command that stops the server
@bot.command()
async def stop(ctx):
    await bot.change_presence(activity=CustomActivity(name="Stopping the Server", type=ActivityType.playing))
    embed=Embed(title=server.StopServer(), color=Color.blue())
    await ctx.send(embed=embed)
    await ctx.send(str(ctx.author.mention))

#Command that gives of the server
@bot.command()
async def status(ctx):
    await bot.change_presence(activity=CustomActivity(name="Sending Server Status", type=ActivityType.playing))
    embed=Embed(title=server.GetStatus(), color=Color.blue())
    await ctx.send(embed=embed)
    await ctx.send(ctx.author.mention)

#Command which gives random headlines from the Indian news pages
@bot.command()
async def headlines(ctx):
    await bot.change_presence(activity=CustomActivity(name="Sending News Headlines", type=ActivityType.playing))
    data = requests.get(url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api).json()
    headlines = data["articles"]
    number = randint(0, len(headlines)-1)
    embed=Embed(title=headlines[number]['title'], url=headlines[number]['url'], color=Color.red())
    url=headlines[number]['urlToImage']
    embed.set_image(url=url)
    await ctx.send(embed=embed)

#Command which provides news for particular topic
@bot.command()
async def sources(ctx, arg):
    await bot.change_presence(activity=CustomActivity(name="Sending News", type=ActivityType.playing))
    data = requests.get(url="https://newsapi.org/v2/everything?q="+arg+"&apiKey="+api).json()
    sources = data['articles']
    number=randint(0, len(sources)-1)
    embed=Embed(title=sources[number]['title'], url=sources[number]['url'], color=Color.red())
    url=sources[number]['urlToImage']
    embed.set_image(url=url)
    await ctx.send(embed=embed)

#Command which provides all the commands that are present in the code
@bot.command()
async def help(ctx):
    await bot.change_presence(activity=CustomActivity(name="Sending help", type=ActivityType.playing))
    embed=Embed(title='Helps/commands of the '+(bot.user.name), description="This Bot is made By Edantuti.",color=Color.dark_blue())
    embed.set_author(name="Developer:Edan Solomon Tuti", url='https://github.com/Edantuti/DiscordBotYOLO')
    embed.add_field(name='News:', value='The command for news:\na!headlines-To show the top headlines in India.\na!sources <query>-To get the news for specific topic.', inline=True)
    embed.add_field(name='Aternos Minecraft:', value='The commands: \na!start-To start the server.\na!stop-To stop the server.\na!status-To get the status of the server.', inline=True)
    await ctx.send(embed=embed)

keep_alive()

token = os.environ.get("DISCORD_TOKEN_SECRET")

bot.run(token)

