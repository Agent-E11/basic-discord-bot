Tutorial Notes
==============

[Online Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-discord-connection)

- I had to install `dotenv` with `pip install python-dotenv` (in previous version)
- v1.5 has `Intents` which need to be specified. `discord.Intents.default()` worked if the bot was an administrator on the channel. Specify the intents in the `Client` constructor:

```py
intents = discord.Intents.default()
client = discord.Client(intents=intents)
```

- To access the contents of messages, you need to enable the `message_content` privileged intent:

```py
intents = discord.Intents.default()
intents.message_content = True
```

- You need to enable the `message_content` privileged intent in the developer portal: Developer portal > Bot > Privileged Gateway Intents

To Do
-----

- Check error messages:
  - Insufficient permissions
  - Wrong GUILD_ID or TOKEN
  - Misconfigured environment variables

- (done) Make the script use environment variables instead of the `.env` file.
