import discord
import random, io, time, asyncio
from discord import app_commands
from discord.ext import commands
from PIL import Image
import requests

from lists.images import images
from lists.names import names

class Race(commands.Cog):
    group = app_commands.Group(name="race",description="For multi-player racing")

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.userScores= {}
        self.index = -1
        self.inRace = False

    #picks a random character and shows them to be ided
    @app_commands.command(name="p",description="Picks a random character's image to be guessed")
    async def p(self, interaction: discord.Interaction):
        await interaction.response.defer()

        self.index = random.randrange(0,len(images))
        url = images[self.index]
        image = Image.open(io.BytesIO(requests.get(url).content))

        with io.BytesIO() as image_binary:
            image.save(image_binary, "PNG")
            image_binary.seek(0)
            return await interaction.followup.send(content="Here you go", file=discord.File(fp=image_binary, filename='image.png'))

    #checks answer against active picture
    @app_commands.command(name="c",description="Checks an answer against active image")
    async def c(self, interaction: discord.Interaction, answer: str):
        if self.index == -1:
            return await interaction.response.send_message(content="There is no active id", ephemeral=True)
        if self.inRace:
            return await interaction.response.send_message(content="There is an active race; you dont need to use the command to check. Just type the name",ephemeral=True)
        if answer.lower() == names[self.index]:
            user_id = interaction.user.id
            if user_id in self.userScores:
                self.userScores[user_id] += 1
            else:
                self.userScores[user_id] = 1
            await interaction.response.send_message(f"{interaction.user.mention} is correct, that was {names[self.index]}.")
            self.index = -1
            return
        
        await interaction.response.send_message(f"incorrect, that was {names[self.index]}")
        self.index = -1
        return 

    #gives a hint for active picture
    @app_commands.command(name="h",description="Gives a hint to the current character in a image")
    async def h(self, interaction: discord.Interaction):
        if self.index == -1:
            return await interaction.response.send_message(content="There is no active image")
        return await interaction.response.send_message(content=f"The first letter is {names[self.index][0]}")

    #gives user score
    @app_commands.command(name="s",description="Gets the score of a player (self if no name specified)")
    async def s(self, interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            member = interaction.user
        if member.id in list(self.userScores.keys()):
            if self.userScores[member.id] > 1:
                return await interaction.response.send_message(content=f"{member.mention} was correct {self.userScores[member.id]} times.")
            return await interaction.response.send_message(f"{member.mention} was correct 1 time.")
        return await interaction.response.send_message(f"{member.mention} has yet to answer correctly.")

    #shows info on inputted character
    @app_commands.command(name="i",description="Shows the info of a character given its name")
    async def i(self, interaction: discord.Interaction, name: str):
        await interaction.response.defer()

        name = name.lower()
        try:
            self.index = names.index(name)
        except ValueError:
            return await interaction.followup.send(content="Not a valid name.",ephemeral=True)
        else:
            image = Image.open(io.BytesIO(requests.get(images[self.index]).content))
            with io.BytesIO() as image_binary:
                image.save(image_binary, "PNG")
                image_binary.seek(0)
                await interaction.followup.send(content=f"This is {names[self.index]}", file=discord.File(fp=image_binary, filename='image.png'))

    #racing
    @group.command(name="start",description="Starts a race with a specified target")
    async def start(self, interaction: discord.Interaction, target: int):
        if self.inRace:
            return await interaction.response.send_message(content="A game cannot be started right now.",ephemeral=True)

        await interaction.response.defer()

        if target > 0:
            self.inRace = True
            correct, incorrect, skips, hints = 0,0,0,0
            startTime = time.time()
            raceScores = {}
            await interaction.followup.send(content=f"First to {target} correct ids wins")

            while True:
                self.index = random.randrange(0,len(images))
                url = images[self.index]
                answer = names[self.index]
                image = Image.open(io.BytesIO(requests.get(url).content))

                with io.BytesIO() as image_binary:
                    image.save(image_binary, "PNG")
                    image_binary.seek(0)
                    await interaction.channel.send(content="here you go", file=discord.File(fp=image_binary, filename='image.png'))

                while True:
                    try:
                        message = await self.bot.wait_for('message',timeout=600)
                    except asyncio.TimeoutError:
                        self.index = -1
                        self.inRace = False
                        return await interaction.channel.send(content=f"Race timed out due to inactivity.")
                    else:

                        if message.content.lower() == "end":
                            if bool(raceScores):
                                winner = max(raceScores, key=lambda item:raceScores[item])
                                await interaction.followup.send(f"<@{winner}> had the highest score of {raceScores[winner]}")
                                self.index = -1
                                self.inRace = False
                            return await interaction.channel.send(content="Game terminated")
                        
                        elif message.content.lower() == "skip":
                            skips += 1
                            await interaction.followup.send(content=f"skipping {names[self.index]}.")
                            break

                        elif message.content.lower() == "hint":
                            hints += 1
                            await interaction.channel.send(f"The first letter is {names[self.index][0]}")

                        elif message.content.lower() == answer:
                            correct += 1
                            await interaction.followup.send(content=f"{message.author.mention} is correct, that was {names[self.index]}")
                            id = message.author.id

                            if id in self.userScores:
                                self.userScores[id] += 1
                            else:
                                self.userScores[id] = 1
                            if id in raceScores:
                                raceScores[id] += 1
                            else:
                                raceScores[id] = 1

                            if raceScores[id] == target:
                                endTime = time.time()
                                self.index = -1
                                self.inRace = False
                                return await interaction.channel.send(content=f"{message.author.mention} has won the race in {int(endTime - startTime)} seconds \n total accuracy was {int(100*(correct/(correct+incorrect)))}% with {hints} hints and {skips} skips used")
                            break

                        elif message.content.lower() in names:
                            incorrect += 1
        else:
            return await interaction.response.send_message(content="input a valid target number to start a race",ephemeral=True)
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Race(bot))