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
intents.message_content = True # Privileged intent
intents.members = True # Privileged intent

client = discord.Client(intents=intents)

# Runs when the bot first connects to the server (successfully)
@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} has connected to the guild:\n'
        f'Name: {guild.name}, ID: {guild.id}'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild members:\n - {members}')

# Runs whenever a member joins
@client.event
async def on_member_join(member):
    # Print to terminal
    print(f'{member.name} joined the server.')
    # Creates a DM channel with the member that just joined and sends them a friendly message
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}. Welcome to the server'
    )

# Runs every time it detects a message
@client.event
async def on_message(message: discord.Message):

    # If the message is a command
    if message.content.startswith('!'):
        # `command` is the first word, `params` is the rest of the words
        command = message.content.split()[0]
        params = message.content.split()[1:]

        print(f'Command: {command}\nParameters: {params}')
    else:
        # If the message mentions a bot
        if "bot" in message.content.lower():
            await client.get_channel(message.channel.id).send('Hello')

    # Print to terminal
    print(f'{message.author.name}: {message.content}')

# Run the client. This method blocks so any code after this will not run
client.run(TOKEN)