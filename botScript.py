import os
import discord

# ----- Load and check variables ----- #
# Load environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

# If either environment variable isn't present, print an error and quit
if TOKEN == None:
    print('Error: No DISCORD_TOKEN environment variable present.')
    quit()

if GUILD_ID == None:
    print('Error: No DISCORD_GUILD_ID environment variable present.')
    quit()

GUILD_ID = int(GUILD_ID)

# Load variables
COMMAND_CHAR = '!'
COMMANDS = [f'{COMMAND_CHAR}help', f'{COMMAND_CHAR}meetingtime']

# Set the intents of the bot, to be given to the `Client` constructor
intents = discord.Intents.default()
intents.message_content = True # Privileged intent
intents.members = True # Privileged intent

client = discord.Client(intents=intents)


# ----- Client event functions ----- #
# Runs when the bot first connects to the server (successfully)
@client.event
async def on_ready():

    guild = client.get_guild(GUILD_ID)

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
        
        # If the message was in the correct guild
        if message.guild != None:
            if message.guild.id == GUILD_ID:
                # `command` is the first word, `params` is the rest of the words
                command = message.content.split()[0]
                params = message.content.split()[1:]
                
                # Get the proper response
                response = handle_command(command, params)

                # Respond in the channel of the original message
                await client.get_channel(message.channel.id).send(response)

                # Log command and parameters
                print(f'Command: {command}\nParameters: {params}')

    elif client.user in message.mentions:
        # If the message mentions the bot, say hello
        await client.get_channel(message.channel.id).send('Hello')


# ----- Generic functions ----- #
# Checks if a word is a command
def is_command(word: str):
    # If it doesn't start with the `COMMAND_CHAR` then it isn't a command
    if not word.startswith(COMMAND_CHAR):
        return False

    # If the word is in `COMMANDS` then it's a command, otherwise, it isn't
    if word in COMMANDS:
        return True
    else:
        return False

# Take a command and its parameters and return the corresponding response
def handle_command(command: str, params: list[str]):

    match command:
        case '!help':
            pretty_commands = '\n'.join(COMMANDS)
            return f'These are some of the commands I can respond to:\n`{pretty_commands}`' # Backticks (`) format text as code in discord
        case '!meetingtime':
            return f'The current meeting time is:\nEvery Wednesday at 5:30pm'


# ----- RUN ----- #
# Run the client. This method blocks so any code after will not run
client.run(TOKEN)
