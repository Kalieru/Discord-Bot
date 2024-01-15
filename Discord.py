import discord
from discord.ext import commands
from Lingo import *

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("---------------------------")

@client.event
async def on_message(Message):
    mess = Message.content
    if mess.startswith("!"):
        words = Permutations(mess[1:])
        if words == []:
            await Message.channel.send(f"No se pueden formar palabras con {mess}")
        else:
            for word in words:
                await Message.channel.send(word)
        return None


client.run("MTE5MjgyNjMwNDg2OTk1NzY2Mg.GVzFld.0-_a8w7lIDXeT3Kvbmg4Gt_yXNECfGIhFDVziw")