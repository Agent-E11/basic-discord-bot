# The default library for the docker image. It will be overwritten by any library file the user might define
import discord
from configparser import ConfigParser

# Echo back to the user what they said.
def command_echo(params: str, message: discord.Message, client: discord.Client, config: ConfigParser):
    if params == '':
        return None
    else:
        return params
