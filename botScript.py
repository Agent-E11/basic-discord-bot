import os

import discord
from dotenv import load_dotenv

# Load environment variables from the `.env` file, set `TOKEN` to the environment variable `DISCORD_TOKEN`.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# If the token isn't present, print an error and quit
if TOKEN == None:
    print("Error: No DISCORD_TOKEN present.")
    quit()

# Set the intents of the bot, to be given to the `Client` constructor
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)