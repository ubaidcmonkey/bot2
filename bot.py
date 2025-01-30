import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user.name}')

bot.run("YOUR_BOT_TOKEN")
