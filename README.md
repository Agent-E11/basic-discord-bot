Basic Discord Bot
=================

This is a basic discord bot, written in Python using the Discord.py module. Its original intent was to make a Discord bot that you can run in a Docker container, but you can also run the script by itself.

It is currently not very customizable, but I am planning on making it more useful in the future.

How to use it
-------------

First, you must [make a Discord application](#), then, [save the bot's token](#).

Then, you should [make a Discord guild](#) ("guild" is the technical term for a Discord server), and [save its ID](#).

There are 2 ways to run the bot script:

- With [Docker](#docker)
- With the standalone [Python script](#python-script-only)

Docker
------

1. Create a `.env` file:
    - In a folder of your choice, create a file called `.env`. In that file, type the following:

        ```.env
        DISCORD_TOKEN=<token>
        DISCORD_GUILD_ID=<guild id>
        ```

    - Replace `<token>` with your bot's token, and replace `<guild id>` with your guild's ID

2. [Install Docker](#)
3. Run this command in the terminal `docker run --rm --env-file ./.env -d --name discord-bot agentell/basic-discord-bot:<tag>`
    - `--rm` means you want the container to be deleted once it stops.
    - `--env-file ./.env` specifies that you wand to load the environment variables defined in the `.env` file into the container.
    - `-d` means that you want to ignore the output of the container (if the command doesn't work the first time, you should try running it without the `-d` flag to see what the error is).
    - `--name discord-bot` means you want to name the container "discord-bot", you can replace "discord-bot" with any name you want.
    - `agentell/basic-discord-bot:<tag>` is the image you want Docker to use when running the container. You must replace `<tag>` with the correct tag though, a safe one to use is `1.1-amd64`.
4. If you set it up correctly, it should just work. But here are some things to try if it didn't (WIP):
    - Permissions
    - ID
    - Environment variables

Python Script Only
------------------
