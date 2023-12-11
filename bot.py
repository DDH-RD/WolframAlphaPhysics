#WolframAlphaBot.py
#A bot that uses the Wolfram Alpha API to answer questions
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'    
        )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name="happy birthday")
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "raise-exception":
        raise discord.DiscordException
    
    elif 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

@bot.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise
path = r"C:\Users\DannyBehr\Documents\WolframAlphaPhysics\err.log"
assert os.path.isfile(path)
with open(path, "r") as f:
    pass

client.run(TOKEN)
bot.run(TOKEN)
#f