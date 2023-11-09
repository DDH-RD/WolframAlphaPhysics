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

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'    
        )
    

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
client.run(TOKEN)

input = input()