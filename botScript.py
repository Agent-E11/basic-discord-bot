import os
from configparser import ConfigParser
import discord
import library
import random

# ----- Load and check variables ----- #
# Initialize ConfigParser
config = ConfigParser()
# Generate the absolute path of the config file (the directory the script is in + the name of the config file)
config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
# Load the configuration settings from the config file.
print(f'Read config file(s): {config.read(config_file_path)}')

# Load variables
TOKEN = config['settings']['token']
GUILD_ID = config.getint('settings', 'guild_id')
COMMAND_CHAR = config['settings'].get('command_prefix', '!')
# `COMMANDS` is the list of commands defined in the config file.
# If the section starts with `command.`, then the command is the second part of that section's name
COMMANDS = [section[8:] for section in config if section.startswith('command.')]
print(f'COMMANDS: {COMMANDS}')

GREETINGS = config['settings'].get('greetings', 'hello|hi').split('|')

# If any of these variables aren't defined, print an error and quit
if TOKEN == None or TOKEN == '':
    print('Error: No `token` defined in config.ini')
    quit()

if GUILD_ID == None or GUILD_ID == '':
    print('Error: No `guild_id` defined in config.ini')
    quit()

if COMMAND_CHAR == None or COMMAND_CHAR == '':
    print('Error: No `command_prefix` defined in config.ini')
    quit()

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
async def on_member_join(member: discord.Member):

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
    if is_command(message.content.split()[0]) and message.author != client.user:
        
        # If the message was in the correct guild
        if message.guild != None:
            if message.guild.id == GUILD_ID:
                # `command` is the first word, `params` is the rest of the words
                command = message.content.split()[0]
                params = message.content.split()[1:]
                
                # Get the proper response
                response = handle_command(command, params)

                # If the command generated a response
                if response != None:
                    # Respond in the channel of the original message
                    await client.get_channel(message.channel.id).send(response)

                # Log command and parameters
                print(f'Command: {command}\nParameters: {params}')

    # If the message mentions the bot and the first word in the message is a "greeting", bot will say hello
    elif client.user in message.mentions and message.content.lower().startswith(tuple(GREETINGS)):
        greeting_response: str = random.choice(GREETINGS)
        await client.get_channel(message.channel.id).send(f'{greeting_response[0].upper() + greeting_response[1:]}, {message.author.display_name}!')


# ----- Generic functions ----- #
# Checks if a word is a command
def is_command(word: str):
    # If it doesn't start with the `COMMAND_CHAR` then it isn't a command
    if not word.startswith(COMMAND_CHAR):
        return False

    # If the word (excluding the command prefix) is in `COMMANDS` then it's a command, otherwise, it isn't
    if word[1:] in COMMANDS:
        return True
    else:
        return False

# Take a command and its parameters and return the corresponding response
def handle_command(command: str, params: list[str]):
    command_section = f'command.{command[1:]}'
    command_type = config[command_section]['type']

    if command_type == 'static':
        # If the command is static
        # Return the content of the given command
        return config[command_section]['content']
    elif command_type == 'dynamic':
        # If the command is dynamic
        # Get the function in `library` that is associated with the command (defined in the config file)
        func = getattr(library, config[command_section]['function'], None)
        if func != None:
            # If the command was successfully retrieved, run it and return its value
            return func(params)
        else:
            # If the command was not present in the `library` module, return None and print an error.
            print(f'The function in the `config.ini` file that is associated with the `{command}` command is not present in `library.py`')
            return None
    else:
        # If the command doesn't have a valid type, return none and print an error
        print(f'The `{command}` command has an invalid type specified in the `config.ini` file')
        return None

# ----- RUN ----- #
# Run the client. This method blocks so any code after will not run
client.run(TOKEN)
