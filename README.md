# Basic Discord Bot #

!!! Disclaimer !!!
This documentation is very out of date. I need to update it. If you want to figure out how it works, you can probably look at the source code, or create a new Discussion. The README might help a little, but don't count on it.

This is a basic discord bot, written in Python using the Discord.py module. Its original intent was to make a Discord bot that you can run in a Docker container, but you can also run the script by itself.

It is currently not very customizable, but I am planning on making it more useful in the future.

---

## How to use it ##

### Make A Discord App ###

First, you must [make a Discord application](https://discordpy.readthedocs.io/en/latest/discord.html), and save the bot's token.

Now, you need to give the bot some privileged intents (you can read more about privileged intents [here](https://discordpy.readthedocs.io/en/stable/intents.html) if you like).

In the [developer portal](https://discord.com/developers/applications), select your application and go to the bot tab. Scroll down to the Privileged Gateway Intents section and enable the following intents:

- Server Members Intent
- Message Content Intent

Save the changes.

Then, you should [make a Discord guild](https://www.ionos.com/digitalguide/server/know-how/how-to-set-up-a-discord-server/) ("guild" is the technical term for a Discord server), and [save its ID](https://www.alphr.com/discord-find-server-id/).

Now, [invite the bot to your server](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot). The bot must have the the following bot permissions (WIP):

- Read messages/View channels
- Send messages
- Send messages in threads
- Read message history

You are now ready to run the script, there are 2 ways to run the bot script:

- With [Docker](#docker)
- With the standalone [Python script](#python-script)

### Docker ###

1. Create a `.env` file:
    - In a folder of your choice, create a file called `.env`. In that file, type the following:

        ```.env
        DISCORD_TOKEN=<token>
        DISCORD_GUILD_ID=<guild id>
        ```

    - Replace `<token>` with your bot's token, and replace `<guild id>` with your guild's ID

2. [Install Docker](https://docs.docker.com/get-docker/)
3. Run this command in [the terminal](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955):
    - `docker run --rm --env-file ./.env -d --name discord-bot agente11/basic-discord-bot:<tag>`

        - `--rm` means you want the container to be deleted once it stops.
        - `--env-file ./.env` specifies that you wand to load the environment variables defined in the `.env` file into the container.
        - `-d` means that you want to ignore the output of the container (if the command doesn't work the first time, you should try running it without the `-d` flag to see what the error is).
        - `--name discord-bot` means you want to name the container "discord-bot", you can replace "discord-bot" with any name you want.
        - `agente11/basic-discord-bot:<tag>` is the image you want Docker to use when running the container. You must replace `<tag>` with the correct tag though, a safe one to use is `1.2-amd64`.

    - You can run `docker ps` to see that the container is running.

4. If you set it up correctly, it should just work. But here are some things to try if it didn't (WIP):
    - Incorrect Permissions
    - Guild ID or Bot Token
    - Environment variables

### Python Script ###

---

## Custom Commands ##
