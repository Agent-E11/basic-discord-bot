Basic Discord Bot
=================
This is a basic discord bot, written in Python using the Discord.py module. Its original intent was to make a Discord bot that you can run in a Docker container, but you can also run the script by itself.

It is currently not very customizable, but I am planning on making it more useful in the future.

How to use it
=============
There are 2 ways to run the bot:
- With [Docker](#docker)
- With the standalone [Python script](#python-script-only)

Docker
------
1. [Create a Discord application](#)
2. [Save the token of your bot](#) (keep this safe)
3. [Make a Discord Guild](#) ("guild" is the technical term for a Discord server)
4. [Save the guild ID](#)
5. Create an `env` file:
    - In a folder of your choice, create a file called `env`. In that file, type the following:

        ```
        DISCORD_TOKEN=<token>
        DISCORD_GUILD_ID=<guild id>
        ```
        Replace `<token>` with your bot's token, and replace `<guild id>` with your guild's ID

6. [Install Docker](#)

Python Script Only
------------------