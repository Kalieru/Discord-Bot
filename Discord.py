import discord
from discord.ext import commands
from Lingo import *
import dotenv
import os

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


dotenv.load_dotenv()
key = os.getenv('KEY')
client.run(key)
