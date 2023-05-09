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
intents.message_content = True

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

@client.event
async def on_member_join(member):
    print(f'{member.name} joined the server.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}. Welcome to the server'
    )

@client.event
async def on_message(message: discord.Message):
    if message.content.isnumeric():
        await client.create_dm()
    print(f'Message sent: {message.content}')

client.run(TOKEN)
