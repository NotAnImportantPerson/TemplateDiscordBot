import discord
from discord.ext import commands

TOKEN = "put here your token"

intents = discord.Intents.default()
intents.message_content = True

# Bot prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f"Bot conected like {bot.user}")

# Template command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

# Start the bot
bot.run(TOKEN)