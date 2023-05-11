import os
import discord
from dotenv import load_dotenv

# Load environment variables from the `.env` file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

# If the token isn't present, print an error and quit
if TOKEN == None:
    print("Error: No DISCORD_TOKEN present.")
    quit()
if GUILD_ID == None:
    print("Error: No DISCORD_GUILD_ID present.")
    quit()

# Load commands
COMMANDS = ['help', 'meetingtime']

# Set the intents of the bot, to be given to the `Client` constructor
intents = discord.Intents.default()
intents.message_content = True # Privileged intent
intents.members = True # Privileged intent

client = discord.Client(intents=intents)

# ----- Client event functions ----- #
# Runs when the bot first connects to the server (successfully)
@client.event
async def on_ready():

    guild: discord.Guild = client.get_guild(GUILD_ID)

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
    # Print message to terminal
    print(f'{message.author.name}: {message.content}')

    # If the message is a command
    if is_command(message.content.split()[0]):
        # `command` is the first word, `params` is the rest of the words
        command = message.content.split()[0]
        params = message.content.split()[1:]

        print(f'Command: {command}\nParameters: {params}')
    else:
        # If the message mentions a bot
        if "bot" in message.content.lower():
            await client.get_channel(message.channel.id).send('Hello')

# ----- Generic functions ----- #

def is_command(word: str):
    if not word.startswith('!'):
        return False
    
    # If the word (not including the first character) is in `COMMANDS` then it's a command
    if word[1:] in COMMANDS:
        return True
    else:
        return False

# ----- RUN ----- #
# Run the client. This method blocks so any code after will not run
client.run(TOKEN)