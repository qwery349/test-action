import os
import discord
from discord.ext import commands

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("👋 Бот работает!")
    await bot.close()  # Закрываем, т.к. GitHub Actions не держит бота постоянно

bot.run(TOKEN)
