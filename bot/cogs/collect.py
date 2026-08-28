import discord
import random, io, time
from discord import app_commands
from discord.ext import commands
from PIL import Image
import requests

from lists.images import images
from lists.names import names
from utils.db import db
from helpers.views import Buttons
from helpers.card import Card

class Collect(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def insertcard(self, userid: int, card: str):
        await db.connect()
        await db.execute("INSERT INTO cards (card_id, user_id) VALUES ($1, $2);",card,userid)
        await db.close()

    async def cardcount(self, name: str) -> int:
        await db.connect()
        retval = await db.execute("SELECT cardnum FROM cardcounts WHERE cardname = $1;",name)
        await db.close()
        if len(retval) == 0:
            return 0
        return retval[0][0]

    async def setcount(self, name: str, num: int):
        await db.connect()
        if (num == 1):
            await db.execute("INSERT INTO cardcounts (cardname, cardnum) VALUES ($1, $2);",name,1)
        else:
            await db.execute("UPDATE cardcounts SET cardnum = $1 WHERE cardname = $2;",num,name)
        await db.close()

    @app_commands.command(name="collection",description="Gets the collection of a user (self if not specified)")
    async def collection(self, interaction: discord.Interaction, user: discord.Member = None):
        if user == None:
            user = interaction.user
        await db.connect()
        retval = await db.execute("SELECT card_id FROM cards WHERE user_id = $1;",user.id)
        await db.close()
        msg = f"{user.mention}'s cards:\n"
        for row in retval:
            msg += ((Card(row[0]).toString())+"\n")
        await interaction.response.send_message(content=msg,ephemeral=True)
        
        
    #picks three random characters and displays them for choosing
    @app_commands.command(name="d",description="A drop of 3 characters!")
    async def d(self, interaction: discord.Interaction):

        lastDropped = 0
        now = time.time_ns()

        await db.connect()
        retval = await db.execute("SELECT dropped_time FROM timeout WHERE user_id = $1;",interaction.user.id)
        if len(retval) == 0:
            await db.execute("INSERT INTO timeout (user_id, dropped_time) VALUES ($1, $2);",interaction.user.id,now)
        else:
            lastDropped = retval[0]['dropped_time']
        await db.close()

        timeRemaining = 18000-((now-lastDropped)/1000000000)

        if timeRemaining > 0:
            return await interaction.response.send_message(content=f"You may drop again in {int(timeRemaining//3600)} hours {int((timeRemaining%3600)//60)} minutes {int(timeRemaining%3600%60)} seconds.",ephemeral=True)
            
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

        await db.connect()
        await db.execute("UPDATE timeout SET dropped_time = $1 WHERE user_id = $2;",now,interaction.user.id)
        await db.close()

        with io.BytesIO() as image_binary:
            imggroup.save(image_binary, "PNG")
            image_binary.seek(0)
            choices = [ names[index1], names[index2], names[index3] ]
            msg = await interaction.followup.send(content=f"{interaction.user.mention}, your drop will be ready soon!")
            view = Buttons(collect=self, names=choices, user=interaction.user, msg=msg)
            return await msg.edit(content=f"{interaction.user.mention}, here is your drop!",attachments=[discord.File(fp=image_binary, filename='image.png')], view=view)

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