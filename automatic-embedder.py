import discord
from discord.ext import commands
import random

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_message(message):
     if message.content.startswith('.'):
      deleted_message = message.content[1:]
      embed = discord.Embed(description=deleted_message + f"\n\nSent by: <@{message.author.id}>",
      color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
      await message.channel.send(embed=embed)
      await message.delete()
      await message.author.send(f"Your message '{deleted_message}' has been deleted and sent as an embed in the channel.")
      print(f"Deleted message from {message.author}: {message.content}")

bot.run('MTA3MjI1OTIyNDkyNDU5NDI2OA.G0o10u.Ga4XSK0FRmS5UGqDTCtCj0P2bFNODkDELXOv0U')