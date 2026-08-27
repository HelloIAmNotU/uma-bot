import discord

class Buttons(discord.ui.View):
    def __init__(self, names: list[str], timeout=45):
        self.names = names
        super().__init__(timeout=timeout)

    async def clicked(self, interaction: discord.Interaction, index):
        await interaction.channel.send(f"{interaction.user.mention} has grabbed {self.names[index]}")
        for child in self.children:
            child.disabled = True
        return await interaction.response.edit_message(view=self)

    @discord.ui.button(label="1",style=discord.ButtonStyle.blurple)
    async def blurple1_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        return await self.clicked(interaction, 0)
    @discord.ui.button(label="2",style=discord.ButtonStyle.blurple)
    async def blurple2_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        return await self.clicked(interaction, 1)
    @discord.ui.button(label="3",style=discord.ButtonStyle.blurple)
    async def blurple3_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        return await self.clicked(interaction, 2)