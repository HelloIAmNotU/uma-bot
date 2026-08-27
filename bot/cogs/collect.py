import discord
import random, io
from discord import app_commands
from discord.ext import commands
from PIL import Image
import requests

from lists.images import images
from lists.names import names
from views.helpers import Buttons

class Collect(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    #picks three random characters and displays them for choosing
    @app_commands.command(name="d",description="A drop of 3 characters!")
    async def d(self, interaction: discord.Interaction):
        await interaction.response.defer()

        index1 = random.randrange(0,len(images))
        index2 = random.randrange(0,len(images))
        index3 = random.randrange(0,len(images))

        image1 = Image.open(io.BytesIO(requests.get(images[index1]).content))
        image2 = Image.open(io.BytesIO(requests.get(images[index2]).content))
        image3 = Image.open(io.BytesIO(requests.get(images[index3]).content))

        x = image1.size[0]
        y = image1.size[1]

        imggroup = Image.new(mode="RGBA", size=(x*3,y), color="white")
        imggroup.paste(image1, (0, 0))
        imggroup.paste(image2, (x, 0))
        imggroup.paste(image3, (x * 2, 0))

        with io.BytesIO() as image_binary:
            imggroup.save(image_binary, "PNG")
            image_binary.seek(0)
            choices = [ names[index1], names[index2], names[index3] ]
            view = Buttons(names=choices)
            return await interaction.followup.send(file=discord.File(fp=image_binary, filename='image.png'), view=view)

    #secret
    @app_commands.command(name="goat",description="Secret...")
    async def goat(self, interaction: discord.Interaction):
        num = random.randrange(0,4)
        match(num):
            case 0:
                return await interaction.response.send_message("https://drive.usercontent.google.com/download?id=1MURrlJVb9euyFF4P-Ro4fNj7IeleXqGG") #falco
            case 1:
                return await interaction.response.send_message("https://drive.usercontent.google.com/download?id=1JC5RmcJKYPJpaIPpg-WoqywjQ5g6FbDp") #teio
            case 2:
                return await interaction.response.send_message("https://drive.usercontent.google.com/download?id=1CtBDc1iXuSCP-KFGQKi9hl2Wvzm6PSQ9") #opera
            case 3:
                return await interaction.response.send_message("https://drive.usercontent.google.com/download?id=1R54xUpNaWt0I_hW1Thn0lVLZgyI9L7c5") #oguri

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Collect(bot))