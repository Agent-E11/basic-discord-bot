import discord
from configparser import ConfigParser

def command_echo(params: str, message: discord.Message, client: discord.Client, config: ConfigParser):
    if params == '':
        return None
    else:
        return params
