#Adding all the necessary functions from the packages
from keep_alive import keep_alive
from aternosapi import AternosAPI
from discord.ext import commands
from discord import Embed, Color, Game, Status
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

@bot.event
async def on_ready():
  await bot.change_presence(status=Status.idle, activity=Game(name="with Discord members", type=3))

#Command which provides all the commands that are present in the code
@bot.command()
async def help(ctx):
    embed=Embed(title='Helps/commands of the '+(bot.user.name), description="This Bot is made By Edantuti.",color=Color.dark_blue())
    embed.set_author(name="Developer:Edan Solomon Tuti", url='https://github.com/Edantuti/DiscordBotYOLO')
    embed.add_field(name='News:', value='The command for news:\na!news headlines-To show the top headlines in India.\na!news sources <query>-To get the news for specific topic.\na!news search <query>-To get the news for the specific topic from varies webstie.', inline=True)
    embed.add_field(name='Aternos Minecraft:', value='The commands: \na!server start-To start the server.\na!server stop-To stop the server.\na!server status-To get the status of the server.', inline=True)
    await ctx.send(embed=embed)

extensions = ['Command', 'Command_Event', 'Server_Command']

for cogs in extensions:
  bot.load_extension(f'{cogs}')

keep_alive()
token = os.environ.get("DISCORD_TOKEN_SECRET")

bot.run(token)

