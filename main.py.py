import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready")

@bot.tree.command(name="hbd", description="Birthday message")
async def hbd(interaction: discord.Interaction, message: str):

    text = f"""Happy Birthday <@949314788964573234> ⋆.𐙚 ̊
　.　　ﾟ .　 ݁ ⠀⠀* ⠀⠀. ˚
{interaction.user.mention} 🩷 Wishes you a happy birthday and says :

{message}

We love you ✿"""

    await interaction.response.send_message("Thank you ✨", ephemeral=True)

    await interaction.channel.send(text)

    embed = discord.Embed(color=0xffb6c1)
    embed.set_image(url="https://i.postimg.cc/ZqsX7px0/6010078794384870475.jpg")

    await interaction.channel.send(embed=embed)

bot.run(TOKEN)
