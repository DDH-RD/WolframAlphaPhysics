#WolframAlphaBot.py
#A bot that uses the Wolfram Alpha API to answer questions
import os
from weakref import ref
import discord
from dotenv import load_dotenv
from pip import main

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        if message.author == client.user:
            return
        else:
            await message.channel.send('Happy Birthday! 🎈🎉')
    


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'    
        )
    

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "raise-exception":
        raise discord.DiscordException
    
    
client.run(TOKEN)