import os

import discord
from dotenv import load_dotenv

# Load environment variables from the `.env` file, set `TOKEN` to the environment variable `DISCORD_TOKEN`.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# If the token isn't present, print an error and quit
if TOKEN == None:
    print("Error: No DISCORD_TOKEN present.")
    quit()

# Set the intents of the bot, to be given to the `Client` constructor
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} has connected to the guild:\n'
        f'Name: {guild.name}, ID: {guild.id}'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild members:\n - {members}')

client.run(TOKEN)