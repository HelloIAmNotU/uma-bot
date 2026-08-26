import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os, time, io, random, requests
from PIL import Image
names = ["admire groove",
         "admire vega",
         "agnes digital",
         "agnes tachyon",
         "air groove",
         "almond eye",
         "aston machan",
         "bamboo memory",
         "biko pegasus",
         "biwa hayahide",
         "bubble gum fellow",
         "buena vista",
         "calstone light o",
         "cesario",
         "cheval grand",
         "copano rickey",
         "curren bouquetdor",
         "curren chan",
         "daiichi ruby",
         "daitaku helios",
         "daiwa scarlet",
         "dantsu flame",
         "dream journey",
         "duramente",
         "durandal",
         "eishin flash",
         "el condor pasa",
         "espoir city",
         "fenomeno",
         "fine motion",
         "forever young",
         "fuji kiseki",
         "fusaichi pandora",
         "gentildonna",
         "gold city",
         "gold ship",
         "grass wonder",
         "haru urara",
         "hishi akebono",
         "hishi amazon",
         "hishi miracle",
         "hokko tarumae",
         "ikuno dictus",
         "inari one",
         "ines fujin",
         "jungle pocket",
         "ks miracle",
         "katsuragi ace",
         "kawakami princess",
         "king halo",
         "kiseki",
         "kitasan black",
         "loves only you",
         "lucky lilac",
         "manhattan cafe",
         "marche lorraine",
         "maruzensky",
         "marvelous sunday",
         "matikanefukukitaru",
         "matikanetannhauser",
         "mayano top gun",
         "meisho doto",
         "mejiro ardan",
         "mejiro bright",
         "mejiro dober",
         "mejiro mcqueen",
         "mejiro palmer",
         "mejiro ramonu",
         "mejiro ryan",
         "mihono bourbon",
         "mr cb",
         "nakayama festa",
         "narita brian",
         "narita taishin",
         "narita top road",
         "neo universe",
         "nice nature",
         "nishino flower",
         "no reason",
         "north flight",
         "oguri cap",
         "orfevre",
         "red desire",
         "rhein kraft",
         "rice shower",
         "royce and royce",
         "rulership",
         "sakura bakushin o",
         "sakura chiyono o",
         "sakura laurel",
         "samson big",
         "satono crown",
         "satono diamond",
         "seeking the pearl",
         "seiun sky",
         "shinko windy",
         "silence suzuka",
         "sirius symboli",
         "smart falcon",
         "sounds of earth",
         "special week",
         "stay gold",
         "still in love",
         "super creek",
         "sweep tosho",
         "symboli kris s",
         "symboli rudolf",
         "tm opera o",
         "taiki shuttle",
         "tamamo cross",
         "tanino gimlet",
         "tap dance city",
         "tokai teio",
         "tosen jordan",
         "transcend",
         "tsurumaru tsuyoshi",
         "twin turbo",
         "verxina",
         "vivlos",
         "vodka",
         "winning ticket",
         "wonder acute",
         "yaeno muteki",
         "yamanin zephyr",
         "yukino bijin",
         "zenno rob roy",]
images = [
         "https://drive.usercontent.google.com/download?id=1kHYWF9JayGWA7VfCscEn44TPANjnNAf8",
         "https://drive.usercontent.google.com/download?id=1ZWfxY-2pbXezCE5cVDrqrF72NO4tpanR",
         "https://drive.usercontent.google.com/download?id=1HxlGUxWPwS1HDYSLPsM1sC91pamHyNLd", #digitan
         "https://drive.usercontent.google.com/download?id=19JYOnP06MfGJnZjRWG8ojkBpnjrxunsJ",
         "https://drive.usercontent.google.com/download?id=18ifsdbkWxyLkmqZAZ73TY9B_ODbYsj3U",
         "https://drive.usercontent.google.com/download?id=1Z-NqJJLU7Yp9ObAN-NRnCX8BIvfyO7L1",
         "https://drive.usercontent.google.com/download?id=1uKvgGUuVC0g71dpoQo4vCEsd31Vpt8NQ",
         "https://drive.usercontent.google.com/download?id=1ObpIgwejXURmzR1VvaZ8mkKvCrXdA2iw",
         "https://drive.usercontent.google.com/download?id=1pZG_-RvTGg6HT5PFMDx6bD1lk5VipWCr",
         "https://drive.usercontent.google.com/download?id=1pE-WFIVGk6F31kMgT1CTC0xaZ2nZ101g",
         "https://drive.usercontent.google.com/download?id=1luAqe0cLj0qn2kjWCRphMeSn-9-V13gr",
         "https://drive.usercontent.google.com/download?id=1ZLDbE4wdUNEyTdzEpbvv9TmSXL5TT9uA",
         "https://drive.usercontent.google.com/download?id=1KzRfHB-d35Aj5CHVZ0R-nssXG8WkKwYw",
         "https://drive.usercontent.google.com/download?id=17reSAf-gk66xBnLeb276ZA4yPOTYHrIq",
         "https://drive.usercontent.google.com/download?id=1EE1EDr0s1w04KMhdz1p79l5q_Mus6LSF",
         "https://drive.usercontent.google.com/download?id=1uInLb1_mgn-Vfl49Yh26wuC0SwcDVNUD", #rickey
         "https://drive.usercontent.google.com/download?id=1AIO88kMi2IVePmgOKXSTIRiwQ8o3dM-o",
         "https://drive.usercontent.google.com/download?id=1bbcXLH8yBcwAEm51PNeCJLfXOKGaT0sn",
         "https://drive.usercontent.google.com/download?id=13megM4l2VjlWZIxqeWv-Z3FAwmO7tIE_",
         "https://drive.usercontent.google.com/download?id=1LpeyPqVNv3hcB69J2SWZhG_DJwlavK5l",
         "https://drive.usercontent.google.com/download?id=1CADgUebj38fHE5EeUSCM972PxePLCBC4",
         "https://drive.usercontent.google.com/download?id=15k6u5s6GEQcvJq7s8noL8RCtMVOqBiUn", #dantsu
         "https://drive.usercontent.google.com/download?id=1o40meoCJ6fc_P7vj0uwGY2C0g-144VHG",
         "https://drive.usercontent.google.com/download?id=1NMPfbVwmiunoLdgaIb2NNQmVhyRL-I5y",
         "https://drive.usercontent.google.com/download?id=1geAV4FhfPti0fDEmL301oapC5UYQAkwv",
         "https://drive.usercontent.google.com/download?id=1KF1K2FmbUTezf7s3AzQD3fIKJ9I20IAr",
         "https://drive.usercontent.google.com/download?id=1jg-oc3Rw0GEweVs96T167IJ5LNOTUZyg",
         "https://drive.usercontent.google.com/download?id=12lNTeONd-72mnKyv0BUNfQrDvMrQesOe",
         "https://drive.usercontent.google.com/download?id=1T5_szwJpqiVJZbMQZYTEXhns8rNUQruL",
         "https://drive.usercontent.google.com/download?id=1Pcu6hwsweT3Z-HCIukSRi3toPzJTVReo", #finemo
         "https://drive.usercontent.google.com/download?id=103FjtnDOn1fQZ7ZTXFM-zqQW6qLoxEvC",
         "https://drive.usercontent.google.com/download?id=1XAVjQdCe-DGObeJ-C7Zdl8RdSFulkh9j",
         "https://drive.usercontent.google.com/download?id=1zyvxL-wl-7NXhVecMsNKtiyReMFpOX_u",
         "https://drive.usercontent.google.com/download?id=1EID_8H2k3ZAEuov0QfUg1MYlBkN98RMs",
         "https://drive.usercontent.google.com/download?id=1AvgNE69bah1yox2m4kR52xYIfPAdcXXs",
         "https://drive.usercontent.google.com/download?id=18T7jS8zfN3WSMet1SJ6LKMQRBWQXJQue", #golshi
         "https://drive.usercontent.google.com/download?id=1yLxr3UdtOl3feMFcdvMOCpkXcoX59Gsh",
         "https://drive.usercontent.google.com/download?id=14ZJpglDcfXyLs2eZseWZfnBTNTFovn3p",
         "https://drive.usercontent.google.com/download?id=18vGoj5_mS9dSCNYlsJ3c6Dfa3cuhkJ5r",
         "https://drive.usercontent.google.com/download?id=1XHZoKRyg42CFUC9OwD0wbUDSq0KvSvBX",
         "https://drive.usercontent.google.com/download?id=1pZftSiAk_PrLw_0ZgmOOkt53BWCNOl13",
         "https://drive.usercontent.google.com/download?id=1UTUg1oxw2N-NLFs_faO_3r3PXxSuxiMt",
         "https://drive.usercontent.google.com/download?id=1NeiI_l9HdsgA9jMPm44WHHl8l9KX_InQ",
         "https://drive.usercontent.google.com/download?id=1TxwlIAS6EIkhmQXt9o5IkGgH7WuJbbV-",
         "https://drive.usercontent.google.com/download?id=1xUT39QzmzPqoEl0X8zbWg3rIQzyyi251",
         "https://drive.usercontent.google.com/download?id=1CIx6iBVyEIK81YR2JbEgvh5iPalwZMdk", #pokke
         "https://drive.usercontent.google.com/download?id=1q3fQM9oGVAWCNRaYc9AxeUlyQNej9pGe",
         "https://drive.usercontent.google.com/download?id=1qGXFhwPK3XbVXNSTtgX_Q_T__cwvmXGq",
         "https://drive.usercontent.google.com/download?id=1jPKS1viOKf3ogKkUxMc7ENle_mI7uLk5",
         "https://drive.usercontent.google.com/download?id=12h1GeAP2hBdvWLiiFvZTatM8OnU-E9GD",
         "https://drive.usercontent.google.com/download?id=1l5kDfc76_JGbkrupNFZS-ugIGYBez8Be",
         "https://drive.usercontent.google.com/download?id=1w0VH7CY2_O3GhKqPqVt15KJq4t0d6tOb", #kita
         "https://drive.usercontent.google.com/download?id=18LNmOjWj_Irguxzjg9xs_AkEw3oIBK2M",
         "https://drive.usercontent.google.com/download?id=1xEU0_mLrdm-w0EXtO2YOKv26gUxXOLnr",
         "https://drive.usercontent.google.com/download?id=1gyIi9u2OhpAfTOhrt_sgiWlWPhvvh7NB",
         "https://drive.usercontent.google.com/download?id=15Fzx-7TAphawPts5nED5AiXX34Yq9POT",
         "https://drive.usercontent.google.com/download?id=10_10ScixikQQXJH0QHS2-mo3MvN386UH",
         "https://drive.usercontent.google.com/download?id=1dkOw4njPBhRpqWaQ2IYPPshpbCbURqWD",
         "https://drive.usercontent.google.com/download?id=1XAoQOJ-TNnSCkkDVwv5z4KGPyZtPMTjd", #fuku
         "https://drive.usercontent.google.com/download?id=1yCGKfce0fZSvX7CDU5f8Yc4P8p8GLiWh",
         "https://drive.usercontent.google.com/download?id=16Ij12KepjfP-mqJqFHtH_UZr4SQrhjVg",
         "https://drive.usercontent.google.com/download?id=1dMhCXFPVyFhQI_kvjxaGbVKbJtUxZrqP",
         "https://drive.usercontent.google.com/download?id=1Brkd-4Hos6SnRY6RPvvL6gbxA1J9fEe2",
         "https://drive.usercontent.google.com/download?id=1_Idss45UMANM2I_kRYRaXkM0K-2ruECi",
         "https://drive.usercontent.google.com/download?id=1qAUFUzBOCGMAfHhC6hRPfwrZwyE4XuNc",
         "https://drive.usercontent.google.com/download?id=1f9XLFvgydsyaeSliLfordEgKa8J1Q6c3",
         "https://drive.usercontent.google.com/download?id=1GF1rfjQzWWwB0EYO4k3z5pnK7sTXkOew", #palmer
         "https://drive.usercontent.google.com/download?id=1x-i5XZmFQzMIGM4MCtjYeBVF84xcdJdE",
         "https://drive.usercontent.google.com/download?id=1a4RNlMeydexstfjoi0rxHsYfAwrW_vfw",
         "https://drive.usercontent.google.com/download?id=1p6VuV14rsTvsmvD7Ecjrmhx-Zwi9tZ4D",
         "https://drive.usercontent.google.com/download?id=15ski4X4zxqjAJkO5qLN2JHpU3Yg9KINz",
         "https://drive.usercontent.google.com/download?id=1eHZD_9CYdI0BmmyNy9h2mQT01jLxpnvd",
         "https://drive.usercontent.google.com/download?id=150u_0nMlktH6LhhqcoAWHUth2FDviHl0",
         "https://drive.usercontent.google.com/download?id=1aFrgs0iy-EzAT6f3aXUdBKdfberkcma0", #taishin
         "https://drive.usercontent.google.com/download?id=1Z1oYWniGafx-sKVGOtJzAMIdSQiaLSgE",
         "https://drive.usercontent.google.com/download?id=1Hu62f56wy7Y8IAutkpwVJl4MziPrV81Z",
         "https://drive.usercontent.google.com/download?id=1p9LeBrVzHvdLmMobsQ8zx-qYKJ5D1h2E", #nature
         "https://drive.usercontent.google.com/download?id=1LUEKc8yzc8zDJdu1_SBxaZCUlUstLpw5",
         "https://drive.usercontent.google.com/download?id=1jIUHr7bx5x-QzX4F11vLLETQWCTJMBfP", #no reason
         "https://drive.usercontent.google.com/download?id=1Pb8a6iH097ZDjZ8ItaSEdbkY3Kf2FZ4T",
         "https://drive.usercontent.google.com/download?id=1R54xUpNaWt0I_hW1Thn0lVLZgyI9L7c5", #oguri
         "https://drive.usercontent.google.com/download?id=1-X1CzLPqVwzmmjxPmdgXfA11H-9cjF_f",
         "https://drive.usercontent.google.com/download?id=1mIO32tevph6OQ3CxvYjJ1jo_YwP1kDtk",
         "https://drive.usercontent.google.com/download?id=1GpQPsabO8QmT__svF7MEldcULKd0Cltp",
         "https://drive.usercontent.google.com/download?id=1puSE7uHMnFADoCtZoTqJTlMTD48tmBx6",
         "https://drive.usercontent.google.com/download?id=1GaA82GjO7rCTDgXeUCvZ5hVRi-ox07hU",
         "https://drive.usercontent.google.com/download?id=1Utd1PSWkZ_mLnpWSCY8QFOUbFmWh-625",
         "https://drive.usercontent.google.com/download?id=1DP1GRWItKJ9ddyRM0iC-P8ydfV8P6DgP",
         "https://drive.usercontent.google.com/download?id=11quQ9mXOGnGDBQJSRCJEMrfASOni8_5Y",
         "https://drive.usercontent.google.com/download?id=1j7wT1tmZDtXtNvNfJ_7ONwBIwOzv5AYV", #laurel
         "https://drive.usercontent.google.com/download?id=18Wv4P6KHIj_mOH8_HbonaPI3WjDeiW10",
         "https://drive.usercontent.google.com/download?id=1MtwJ2bihnfr_XYj8tHddb1XukYakTJyM",
         "https://drive.usercontent.google.com/download?id=1ajBz7Ox_EVW0ezJEgKmXWAAFIVjlMkAI",
         "https://drive.usercontent.google.com/download?id=1iNorWCBGRU5vw9q5s-AkNhyzaAvqh-bo",
         "https://drive.usercontent.google.com/download?id=1-Bu0hXKO2uXJCiN7Xa-uG3eenBA6ymEt",
         "https://drive.usercontent.google.com/download?id=1dGN0iuSQwJ8VwlqDs0wTgDGJs4Mopp5G",
         "https://drive.usercontent.google.com/download?id=1hLt0zuoBYqqywnpMRa_flSKT5VVncyPv",
         "https://drive.usercontent.google.com/download?id=1X_10oHiwTTKySQGWaq2qL_1oSVypj1hp",
         "https://drive.usercontent.google.com/download?id=1MURrlJVb9euyFF4P-Ro4fNj7IeleXqGG", #falco
         "https://drive.usercontent.google.com/download?id=1vtdM8vaLJbrKoIrGkBRZdkiE3Xzpe8c3",
         "https://drive.usercontent.google.com/download?id=1aH9D1C7KGFRIWrX5t8o_kBC5OlyzugdT",
         "https://drive.usercontent.google.com/download?id=134_cKhUMvc2Lk0pAQwWGU8TMEBGO_XoY",
         "https://drive.usercontent.google.com/download?id=1qAPdeLYOjvzHUFdJXBEo9GToPcKSkWw5",
         "https://drive.usercontent.google.com/download?id=1gurHGUTG4INiKZtIlQ3529I3kCAcPagv",
         "https://drive.usercontent.google.com/download?id=1Aczcey_XqS2jX6kThlao_6zw78F1Onb9",
         "https://drive.usercontent.google.com/download?id=1kHOU15f9RcjYgTB86n5WipF5NLHLO0gy",
         "https://drive.usercontent.google.com/download?id=1M6WQ2EflyFH5HTFGtsXNaOENwkgk11-T",
         "https://drive.usercontent.google.com/download?id=1CtBDc1iXuSCP-KFGQKi9hl2Wvzm6PSQ9", #opera
         "https://drive.usercontent.google.com/download?id=132Jsr1c9PaBAJEvFDnM9DEmIoR59GvXW",
         "https://drive.usercontent.google.com/download?id=180SbkLHLcClcJ-zJRUlXuip9wrFl1PTL",
         "https://drive.usercontent.google.com/download?id=14VE7lazuKuCr4yEo7waHHWh3c8URRzGv",
         "https://drive.usercontent.google.com/download?id=1unh7bNvutf6EEsPca3qu66Vu_jsorr74",
         "https://drive.usercontent.google.com/download?id=1JC5RmcJKYPJpaIPpg-WoqywjQ5g6FbDp", #teio
         "https://drive.usercontent.google.com/download?id=16r-yFawTjauIkfW1R4J8zUuGPDWLuFI3",
         "https://drive.usercontent.google.com/download?id=1m-aLNzqZYDPMSC7Kr6ZGcLB3Ny1sVkr6",
         "https://drive.usercontent.google.com/download?id=1Z2PTe4ShV7geQaRPXzlyPXX-GKbfo9tj",
         "https://drive.usercontent.google.com/download?id=1ew9P-YZG-9oKBuQ_VMJhzlgxC1VaPrC1",
         "https://drive.usercontent.google.com/download?id=1t0TxjXZv5sCVe0HcwpVP1XoZf_TJv8ij",
         "https://drive.usercontent.google.com/download?id=1WvqBD_tAQ40CowgSHZFd-ORHb2SkPzmk",
         "https://drive.usercontent.google.com/download?id=15T3mrPUnP_Caczvh16lo7O-7tihp2uXx", #vodka
         "https://drive.usercontent.google.com/download?id=1lu9gi6HnEdDO_uNSwSqeDPQDC4R37GxO",
         "https://drive.usercontent.google.com/download?id=1Al1kd4afE7ZzoM8PuBKhEPJoxVEkL8Wi",
         "https://drive.usercontent.google.com/download?id=1UPYdAvSjAHQecVSxNaP_N9hqM_7z7K_E",
         "https://drive.usercontent.google.com/download?id=1gdzX3SS7yCBn9Zkoo6xPecqAN7SouZNl",
         "https://drive.usercontent.google.com/download?id=1SCh7hNlKK8U6oq6TBRWoplhsNEKVEsLy",
         "https://drive.usercontent.google.com/download?id=1T47-TT17nNXXpJeOzH7BCwjIiFGFEbGo"]

userScores = {}
raceScores = {}
index = -1
inRace = False
raceAmt = 0
startTime = time.time()
correct, incorrect, skips, hints = 0,0,0,0

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='u.', intents=intents)

#startup command to see when bot is ready to go
@bot.event
async def on_ready():
    print(len(names))
    print(len(images))

#makes bot not respond to itself
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=45):
        super().__init__(timeout=timeout)
    async def clicked(self, interaction: discord.Interaction, index):
        await interaction.channel.send(
            f"{interaction.user.mention} has grabbed {names[index]}"
        )
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="1",style=discord.ButtonStyle.blurple)
    async def blurple1_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await self.clicked(interaction, index1)
    @discord.ui.button(label="2",style=discord.ButtonStyle.blurple)
    async def blurple2_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await self.clicked(interaction, index2)
    @discord.ui.button(label="3",style=discord.ButtonStyle.blurple)
    async def blurple3_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await self.clicked(interaction, index3)

@bot.command()
async def button(ctx):
    view=Buttons()
    await ctx.send("This message has buttons!",view=view)

#picks a random character and shows them to be ided
@bot.command()
async def p(ctx):
    global index
    image = random.choice(images)
    index = images.index(image)
    image = Image.open(io.BytesIO(requests.get(image).content))
    with io.BytesIO() as image_binary:
        image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send("here you go", file=discord.File(fp=image_binary, filename='image.png'))

#gives a hint for active picture
@bot.command()
async def h(ctx):
    if index == -1:
        await ctx.send(f"there is no active id")
    else:
        await ctx.send(f"the first letter is {names[index][0]}")

#checks answer against active picture
@bot.command()
async def c(ctx, *, msg):
    global index, userScores
    if index == -1:
        await ctx.send(f"there is no active id")
        return
    if inRace:
        await ctx.send(f"there is an active race, you dont need to use the command to check, just type the name")
        return
    if msg.lower() == names[index]:
        await ctx.send(f"{ctx.author.mention} is correct, that was {names[index]}")
        user = ctx.author.id
        if user in userScores:
            userScores.update({user: userScores[user]+1})
        else:
            userScores.update({user: 1})
        index = -1
        return
    if msg != names[index]:
        await ctx.send(f"incorrect, that was {names[index]}")
        index = -1

#gives user score
@bot.command()
async def s(ctx, *, msg = ""):
    if msg == "":
        if ctx.author.id in userScores:
            if userScores[ctx.author.id] > 1:
                await ctx.send(f"{ctx.author.mention} was correct {userScores[ctx.author.id]} times")
            else:
                await ctx.send(f"{ctx.author.mention} was correct 1 time")
        else:
            await ctx.send(f"{ctx.author.mention} has yet to answer correctly")
    else:
        name = msg
        name = name.replace("<", "")
        name = name.replace(">", "")
        name = name.replace("@", "")
        if int(name) in userScores:
            if userScores[int(name)] > 1:
                await ctx.send(f"{msg} was correct {userScores[int(name)]} times")
            else:
                await ctx.send(f"{msg} was correct 1 time")
        else:
            await ctx.send(f"{msg} has yet to answer correctly")

#shows info on inputted character
@bot.command()
async def i(ctx, *, msg):
    msg = msg.lower()
    if msg in names:
        index = names.index(msg)
        image = Image.open(io.BytesIO(requests.get(images[index]).content))
        with io.BytesIO() as image_binary:
            image.save(image_binary, "PNG")
            image_binary.seek(0)
            await ctx.send(f"this is {names[index]}", file=discord.File(fp=image_binary, filename='image.png'))
    else:
        await ctx.send(f"not a valid name")

#idea credit to Lucas Li - https://github.com/HelloIAmNotU/image-guess-bot
#picks three random characters and displays them for choosing
@bot.command()
async def d(ctx):
    global index1
    global index2
    global index3
    index1 = images.index(random.choice(images))
    index2 = images.index(random.choice(images))
    index3 = images.index(random.choice(images))
    image1 = Image.open(io.BytesIO(requests.get(images[index1]).content))
    image2 = Image.open(io.BytesIO(requests.get(images[index2]).content))
    image3 = Image.open(io.BytesIO(requests.get(images[index3]).content))
    x = image1.size[0]
    y = image1.size[1]
    imggroup = Image.new(mode="RGB", size=(x * 3, y), color="white")
    imggroup.paste(image1, (0, 0), image1)
    imggroup.paste(image2, (x, 0), image2)
    imggroup.paste(image3, (x * 2, 0), image3)
    with io.BytesIO() as image_binary:
        imggroup.save(image_binary, "PNG")
        image_binary.seek(0)
        view = Buttons()
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'), view=view)
    return

#lists all characters - testing only
@bot.command()
async def list(ctx):
    sortedlist = names.copy()
    sortedlist.sort()
    sentlist = "\n".join(sortedlist)
    await ctx.send(sentlist)

#secret
@bot.command()
async def goat(ctx):
    num = random.randint(0,3)
    if num == 0:
        await ctx.send("https://drive.usercontent.google.com/download?id=1MURrlJVb9euyFF4P-Ro4fNj7IeleXqGG") #falco
    if num == 1:
        await ctx.send("https://drive.usercontent.google.com/download?id=1JC5RmcJKYPJpaIPpg-WoqywjQ5g6FbDp") #teio
    if num == 2:
        await ctx.send("https://drive.usercontent.google.com/download?id=1CtBDc1iXuSCP-KFGQKi9hl2Wvzm6PSQ9") #opera
    if num == 3:
        await ctx.send("https://drive.usercontent.google.com/download?id=1R54xUpNaWt0I_hW1Thn0lVLZgyI9L7c5") #oguri

#racing
@bot.command()
async def r(ctx, *, msg=""):
    global inRace, raceAmt, raceScores, index, startTime
    if len(msg) > 5:
        msg = msg.split()
        msg1 = msg[0]
        msg2 = msg[1]
        if msg1 == "start":
            if int(msg2) > 0:
                inRace = True
                raceAmt = int(msg2)
                startTime = time.time()
                await ctx.send(f"first to {raceAmt} correct ids wins")
                image = random.choice(images)
                index = images.index(image)
                image = Image.open(io.BytesIO(requests.get(image).content))
                with io.BytesIO() as image_binary:
                    image.save(image_binary, "PNG")
                    image_binary.seek(0)
                    await ctx.send("here you go", file=discord.File(fp=image_binary, filename='image.png'))
                return
    if str(msg) == "stop" and inRace:
        if bool(raceScores):
            winner = max(raceScores, key=lambda item:raceScores[item])
            await ctx.send(f"race stopped, <@{winner}> had the highest score of {raceScores[winner]}")
            inRace = False
            raceAmt = 0
            raceScores.clear()
        else:
            await ctx.send(f"race stopped")
    else:
        await ctx.send("input a valid number to start a race")

#message checks for during race
@bot.event
async def on_message(message):
    global index, raceAmt, userScores, raceScores, inRace, correct, incorrect, skips, hints
    if message.author == bot.user:
        return
    if inRace:
        if message.content.lower() in names:
            if message.content.lower() == names[index]:
                correct += 1
                await message.channel.send(f"{message.author.mention} is correct, that was {names[index]}")
                user = message.author.id
                if user in userScores:
                    userScores.update({user: userScores[user] + 1})
                else:
                    userScores.update({user: 1})
                if user in raceScores:
                    raceScores.update({user: raceScores[user] + 1})
                else:
                    raceScores.update({user: 1})
                if int(raceScores[user]) < raceAmt:
                    image = random.choice(images)
                    index = images.index(image)
                    image = Image.open(io.BytesIO(requests.get(image).content))
                    with io.BytesIO() as image_binary:
                        image.save(image_binary, "PNG")
                        image_binary.seek(0)
                        await message.channel.send("here you go", file=discord.File(fp=image_binary, filename='image.png'))
                else:
                    endTime = time.time()
                    await message.channel.send(f"{message.author.mention} has won the race in {int(endTime - startTime)} seconds \n total accuracy was {int(100*(correct/(correct+incorrect)))}% with {hints} hints and {skips} skips used")
                    raceScores.clear()
                    index = -1
                    inRace = False
                    raceAmt = 0
                    correct, incorrect, skips, hints = 0, 0, 0, 0
            else:
                await message.channel.send("incorrect")
                incorrect += 1
        if message.content.lower() == "skip":
            skips += 1
            await message.channel.send(f"skipping {names[index]}")
            image = random.choice(images)
            index = images.index(image)
            image = Image.open(io.BytesIO(requests.get(image).content))
            with io.BytesIO() as image_binary:
                image.save(image_binary, "PNG")
                image_binary.seek(0)
                await message.channel.send("here you go", file=discord.File(fp=image_binary, filename='image.png'))
        if message.content.lower() == "hint":
            hints += 1
            await message.channel.send(f"the first letter is {names[index][0]}")
    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)